from django import forms
from .models import Exam, Grade

# Form to create/edit an exam
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'subject', 'date', 'duration', 'max_marks']

# Form to input grades (optional, not strictly needed if handled in the view)
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['marks_obtained', 'grade']
