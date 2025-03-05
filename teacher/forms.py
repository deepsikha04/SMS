from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'subjects_taught', 'date_of_hire', 'availability']
