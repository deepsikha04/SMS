from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    # Admin: Create and manage classes
    path('create/', views.create_class, name='create_class'),
    path('schedule/create/', views.create_class_schedule, name='create_class_schedule'),
    path('manage/', views.manage_classes, name='manage_classes'),
    
    # Student: View classes and enroll
    path('view/', views.view_classes, name='view_classes'),
    path('enroll/<int:class_id>/', views.enroll_in_class, name='enroll_in_class'),
    
    # View class schedule
    path('schedule/<int:class_id>/', views.view_class_schedule, name='view_class_schedule'),
]
