from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("<int:pk>/", views.student_detail, name="student_detail"),
    path("<int:student_id>/add_record/", views.add_academic_record, name="add_academic_record"),
]
