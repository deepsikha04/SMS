from django import forms
from .models import Attendance, Grade


class AttendanceFilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    student = forms.CharField(max_length=100, required=False)


class GradeFilterForm(forms.Form):
    student = forms.CharField(max_length=100, required=False)
    subject = forms.CharField(max_length=100, required=False)
