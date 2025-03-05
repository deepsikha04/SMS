from django.contrib import admin
from .models import Parent, Student, AcademicRecord, Enrollment

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'dob', 'enrollment_date', 'guardian')
    list_filter = ('enrollment_date', 'dob')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
    autocomplete_fields = ['guardian']
    ordering = ('first_name', 'last_name')


@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'grades', 'notes')
    search_fields = ('student__first_name', 'student__last_name', 'grades')
    list_filter = ('student',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'enrolled_class', 'enrollment_date')
    list_filter = ('enrollment_date', 'enrolled_class')
    search_fields = ('student__first_name', 'student__last_name', 'enrolled_class__name')
    autocomplete_fields = ['student', 'enrolled_class']
