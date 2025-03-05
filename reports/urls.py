from django.urls import path
from . import views

urlpatterns = [
    path('student-performance/', views.student_performance_report, name='student_performance_report'),
    path('student-attendance/', views.student_attendance_report, name='student_attendance_report'),
    path('class-schedule/', views.class_schedule_report, name='class_schedule_report'),
]
