from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'enrolled_class', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('student__first_name', 'student__last_name', 'enrolled_class__enrolled_class__class_name')
