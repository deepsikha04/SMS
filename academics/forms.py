from django import forms
from .models import Student, AcademicRecord

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "date_of_birth", "student_id"]

class AcademicRecordForm(forms.ModelForm):
    class Meta:
        model = AcademicRecord
        fields = ["subject", "grade", "year"]
