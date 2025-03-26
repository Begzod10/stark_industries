import pprint
import socket
import threading
import time
from datetime import datetime

from django.db import DatabaseError
from django.utils import timezone  # Add this for timezone-aware datetimes

from device.models import Device
from users.models.analysis import UserAnalysis, AnalysisResult

# ASCII control characters
ENQ = chr(0x05)
ACK = chr(0x06)
STX = chr(0x02)
ETX = chr(0x03)
EOT = chr(0x04)
CR = chr(0x0D)


class MaglumiX3Server:
    def __init__(self, device_id):
        try:
            self.device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            raise ValueError(f"Device with ID {device_id} does not exist")

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server.bind((self.device.ip_address, self.device.port))
        except OSError as e:
            raise OSError(f"Failed to bind {self.device.ip_address}:{self.device.port} - {str(e)}")

        self.server.listen(5)
        print(f"Server started for {self.device.name}: {self.device.ip_address}:{self.device.port}")

        self.transmitter_name = self.device.name
        self.receiver_name = self.device.receiver_name
        self.password = self.device.password
        self.protocol_version = self.device.protocol_version

    def send_message(self, conn, message):
        print(f"Sending: {repr(message)}")
        conn.send(message.encode('ascii'))
        response = conn.recv(1024).decode('ascii', errors='ignore')
        if response == ACK:
            print("ACK received")
            return True
        else:
            print(f"ACK not received, got: {repr(response)}")
            return False

    def receive_message(self, conn):
        data = conn.recv(1).decode('ascii', errors='ignore')
        if not data:
            return None
        if data == ENQ:
            print("ENQ received, sending ACK")
            conn.send(ACK.encode('ascii'))
            message = ""
            while True:
                chunk = conn.recv(4096).decode('ascii', errors='ignore')
                if not chunk:
                    break
                message += chunk
                if EOT in chunk:
                    print("EOT received")
                    break
            return message
        print(f"Unexpected data: {repr(data)}")
        return None

    def create_header(self, date):
        return f"H|\\^&||{self.password}|{self.transmitter_name}|||||{self.receiver_name}||P|{self.protocol_version}|{date}{CR}"

    def create_patient_record(self, serial_no):
        return f"P|{serial_no}{CR}"

    def create_test_assay_record(self, serial_no, sample_no, assay_name):
        return f"O|{serial_no}|{sample_no}||^^^{assay_name}|R{CR}"

    def create_termination_record(self, serial_no):
        return f"L|{serial_no}|N{CR}"

    def parse_and_save_results(self, message):
        clean_message = message.replace(STX, '').replace(ETX, '').replace(EOT, '')
        lines = clean_message.split(CR)

        results = []
        current_order = None

        for line in lines:
            if line.strip():
                if line.startswith("O|"):
                    parts = line.split("|")
                    if len(parts) > 4:
                        current_order = {
                            'sample_no': parts[2],
                            'test_code': parts[4].replace("^^^", "")
                        }
                elif line.startswith("R|") and current_order:
                    parts = line.split("|")
                    if len(parts) > 7:
                        timestamp = parts[-1]
                        simple_time = None
                        if timestamp and len(timestamp) == 14:
                            try:
                                naive_time = datetime.strptime(timestamp, "%Y%m%d%H%M%S")  # Fixed format
                                simple_time = timezone.make_aware(naive_time)  # Make timezone-aware
                            except ValueError:
                                simple_time = timezone.now()  # Use timezone-aware now()

                        try:
                            user_analysis = UserAnalysis.objects.get(id=int(current_order['sample_no']))
                            analysis = user_analysis.analysis.filter(code_name=current_order['test_code']).first()
                            if analysis:
                                AnalysisResult.objects.create(
                                    user_analysis=user_analysis,
                                    analysis=analysis,
                                    result=parts[3],
                                    timestamp=simple_time or timezone.now(),  # Always timezone-aware
                                    units=parts[4]
                                )
                                user_analysis.status = 2
                                user_analysis.save()
                                results.append({
                                    'sample_no': current_order['sample_no'],
                                    'test_code': current_order['test_code'],
                                    'result': parts[3],
                                    'units': parts[4],
                                    'timestamp': simple_time or timezone.now()
                                })
                            else:
                                print(f"Test code mismatch: {current_order['test_code']} not found")
                        except UserAnalysis.DoesNotExist:
                            print(f"No UserAnalysis found for ID {current_order['sample_no']}")
                        except DatabaseError as e:
                            print(f"Database error saving result: {e}")
                        except Exception as e:
                            print(f"Error saving result: {e}")

        return results

    def send_test_assays(self, conn, sample_no):
        try:
            user_analysis = UserAnalysis.objects.filter(id=int(sample_no)).first()
            if not user_analysis or not user_analysis.analysis.exists():
                print(f"No UserAnalysis or Analysis found for sample {sample_no}")
                conn.send(ACK.encode('ascii'))
                return

            assays = list(user_analysis.analysis.values_list('code_name', flat=True))
        except ValueError:
            print(f"Invalid sample_no: {sample_no}")
            conn.send(ACK.encode('ascii'))
            return

        if not assays:
            print(f"No tests found for sample {sample_no}")
            conn.send(ACK.encode('ascii'))
            return

        message = (
                STX +
                self.create_header(time.strftime("%Y%m%d%H%M%S")) +
                self.create_patient_record("1")
        )
        for i, assay in enumerate(assays, 1):
            message += self.create_test_assay_record(i, sample_no, assay)
        message += self.create_termination_record("1") + ETX + EOT
        self.send_message(conn, message)

    def handle_client(self, conn, addr):
        print(f"Client connected to {self.device.name}: {addr}")
        try:
            while True:
                message = self.receive_message(conn)
                if message is None:
                    continue

                if "Q|" in message:
                    lines = message.split(CR)
                    for line in lines:
                        if line.startswith("Q|"):
                            parts = line.split("|")
                            if len(parts) > 2:
                                sample_no = parts[2].replace("^", "")
                                print(f"Sample ID received for {self.device.name}: {sample_no}")
                                self.send_test_assays(conn, sample_no)

                elif "R|" in message:
                    print(f"Results received for {self.device.name}:")
                    print(repr(message))
                    results = self.parse_and_save_results(message)
                    print("Saved results:")
                    pprint.pprint(results)
                    conn.send(ACK.encode('ascii'))
                    print("ACK sent")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
            print(f"Client disconnected from {self.device.name}: {addr}")

    def start_server(self):
        while self.device.is_active and not self.device.deleted:
            try:
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)
                thread.start()
            except Exception as e:
                print(f"Error accepting connection: {e}")

    def close(self):
        self.server.close()


def run_servers():
    active_devices = Device.objects.filter(is_active=True, deleted=False, brand__name="SNIBE")
    threads = []

    for device in active_devices:
        try:
            server = MaglumiX3Server(device.id)
            thread = threading.Thread(target=server.start_server, daemon=True)
            threads.append(thread)
            thread.start()
        except OSError as e:
            print(f"Failed to start server for {device.name} ({device.ip_address}:{device.port}): {e}")
        except Exception as e:
            print(f"Unexpected error starting server for {device.name}: {e}")

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stark_industry.settings")
    import django

    django.setup()
    run_servers()
