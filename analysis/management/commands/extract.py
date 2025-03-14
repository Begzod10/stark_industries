import re

from django.core.management.base import BaseCommand
from docx import Document

from analysis.models import AnalysisType, Analysis
from device.models import Device


class Command(BaseCommand):
    help = 'DOCX faylini o\'qib, analiz turlari va narxlarini ma\'lumotlar bazasiga import qilish'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='DOCX fayl manzili')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        category_data = self.read_docx_and_separate(file_path)

        self.print_analysis_data(category_data)

    def read_docx_and_separate(self, file_path):
        doc = Document(file_path)

        current_category = None
        category_data = {}

        for table in doc.tables:
            for row in table.rows:
                if len(row.cells) >= 3:  # Har bir satrda kamida 3 hujayra bo'lishi kerak
                    first_cell = row.cells[0].text.strip()  # 0-chi yacheyka (turkum)
                    second_cell = row.cells[1].text.strip()  # 1-chi yacheyka (analiz turi)
                    third_cell = row.cells[2].text.strip()  # 2-chi yacheyka (narx)

                    if first_cell == "" and third_cell == "":
                        current_category = second_cell
                        if current_category not in category_data:
                            category_data[current_category] = {"with_price": [], "no_price": []}

                    elif second_cell != "" and third_cell != "":
                        category_data[current_category]["with_price"].append((second_cell, third_cell))

                    elif second_cell != "" and third_cell == "":
                        category_data[current_category]["no_price"].append(second_cell)

        return category_data

    def print_analysis_data(self, category_data):
        for category, data in category_data.items():

            if data["with_price"]:
                for analysis_type, price in data["with_price"]:
                    match = re.findall(r'\d+-\d+', analysis_type)
                    if match:
                        device, created = Device.objects.get_or_create(name=match[0],
                                                                       defaults={'ip_address': '38.0.101.76'},
                                                                       branch_id=1)
                        analysis_type_instance, created_analysis_type = AnalysisType.objects.get_or_create(
                            name=category)
                        price = price.replace(" ", "")

                        analysis, created_analysis = Analysis.objects.get_or_create(
                            type=analysis_type_instance,
                            device=device,
                            name=analysis_type_instance.name,
                            price=price
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f"Device yaratildi: {device.name}"))
                        if created_analysis_type:
                            self.stdout.write(
                                self.style.SUCCESS(f"AnalysisType yaratildi: {analysis_type_instance.name}"))
                        if created_analysis:
                            self.stdout.write(self.style.SUCCESS(f"Analysis yaratildi: {analysis.name}"))
# example to run
# python manage.py extract C:\Users\sunna\PycharmProjects\stark_industries\analysis\management\commands\analiz.docx
