from django.contrib import admin
from .models import Teacher, ClassAssignment, TeacherSchedule

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'date_of_hire')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date_of_hire',)

@admin.register(ClassAssignment)
class ClassAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'assigned_class', 'assigned_date')
    search_fields = ('teacher__first_name', 'teacher__last_name', 'assigned_class__class_name')
    list_filter = ('assigned_date',)

@admin.register(TeacherSchedule)
class TeacherScheduleAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'class_instance', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('teacher__first_name', 'teacher__last_name', 'class_instance__class_name')
    list_filter = ('day_of_week',)

