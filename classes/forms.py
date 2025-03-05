from django import forms
from .models import Class, ClassSchedule

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'description', 'start_time', 'end_time', 'capacity']


class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['class_instance', 'day_of_week', 'start_time', 'end_time']
