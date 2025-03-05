from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('dashboard')

urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')), 
    path('student/', include('students.urls')), 
    path('teacher/', include('teacher.urls')), 
    path('class/', include('classes.urls')), 
    path('academic/', include('academics.urls')), 
    path('attendance/', include('attendance.urls')), 
    path('exam/', include('exam.urls')), 
    path('library/', include('library.urls')), 
    path('reports/', include('reports.urls')), 
]