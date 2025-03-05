from django.contrib import admin
from .models import Class, ClassSchedule

# Register the Class model if it's not already registered
if not admin.site.is_registered(Class):
    class ClassAdmin(admin.ModelAdmin):
        list_display = ('class_name', 'description', 'start_time', 'end_time', 'capacity')
        search_fields = ('class_name', 'description')
        list_filter = ('start_time', 'end_time')
        ordering = ('class_name',)

    admin.site.register(Class, ClassAdmin)
else:
    print("Class model is already registered with admin.")

# Register ClassSchedule model
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_instance', 'day_of_week', 'start_time', 'end_time')
    search_fields = ('class_instance__class_name', 'day_of_week')
    list_filter = ('day_of_week',)
    ordering = ('class_instance', 'day_of_week')

admin.site.register(ClassSchedule, ClassScheduleAdmin)
