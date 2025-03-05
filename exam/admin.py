from django.contrib import admin
from .models import Subject, Exam, StudentExam, Grade

# Register your models here.
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(StudentExam)
admin.site.register(Grade)
