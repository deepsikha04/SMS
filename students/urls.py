from django.urls import path

from . import views
from django.shortcuts import render

def home(request):
     return render (request, 'frontend/home.html')

# students/urls.py


app_name = 'students'

urlpatterns = [
    path('manage-students/', views.manage_students, name='manage_students'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('enroll-student/<int:student_id>/', views.enroll_student, name='enroll_student'),
    
]




