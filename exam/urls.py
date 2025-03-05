from django.urls import path
from .views import ExamListView, ExamCreateView, GradeInputView, ReportCardView
from . import views

app_name = 'exam'

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam_list'),
    path('exams/create/', ExamCreateView.as_view(), name='exam_create'),
    path('exams/<int:exam_id>/grade/', GradeInputView.as_view(), name='grade_input'),
    path('report_card/<int:student_id>/', ReportCardView.as_view(), name='report_card'),
     path('create/', views.ExamCreateView.as_view(), name='exam_create'),
]
