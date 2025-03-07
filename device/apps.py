import threading

from django.apps import AppConfig


class DeviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'device'

    def ready(self):
        from device.server.snibe import run_servers
        if not hasattr(self, 'server_thread'):
            self.server_thread = threading.Thread(target=run_servers, daemon=True)
            self.server_thread.start()
            print("ASTM servers started in background")
