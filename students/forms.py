# students/forms.py
from django import forms
from .models import Student, AcademicRecord, Enrollment
from classes.models import Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'contact_number', 'email', 'guardian']

class AcademicRecordForm(forms.ModelForm):
    class Meta:
        model = AcademicRecord
        fields = ['grades', 'notes']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['enrolled_class']
