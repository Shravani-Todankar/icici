from django.contrib import admin
from .models import PDF
# Register your models here.
from .models import QuizQuestion, QuizResult

admin.site.register(QuizQuestion)
admin.site.register(QuizResult)
admin.site.register(PDF)
# admin.site.register(QuizQuestion)





