from django.urls import path
from .views import register_view, login_view, logout_view, admin_dashboard, teacher_dashboard, role_redirect



urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('role-redirect/', role_redirect, name='role_redirect'),

]
