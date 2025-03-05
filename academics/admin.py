from django.contrib import admin
from .models import Student, AcademicRecord

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "student_id"]

@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "grade", "year", "created_by"]
