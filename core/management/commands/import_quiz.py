from django.core.management.base import BaseCommand
import openpyxl
from core.models import QuizQuestion


class Command(BaseCommand):
    help = 'Import quiz questions from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        filepath = kwargs['filepath']
        wb = openpyxl.load_workbook(filepath)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0] and row[5]:  # Make sure question and answer exist
                question = row[0]
                option_a = row[1]
                option_b = row[2]
                option_c = row[3]
                option_d = row[4]
                correct_answer = str(row[5]).strip().upper()

                QuizQuestion.objects.create(
                    question=question,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                    correct_answer=correct_answer
                )

        self.stdout.write(self.style.SUCCESS('✅ Quiz questions imported successfully!'))
