from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# User Registration
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('role_redirect')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

# User Logout
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

# Redirect based on role
@login_required
def role_redirect(request):
    if request.user.is_admin():
        return redirect('admin_dashboard')
    elif request.user.is_teacher():
        return redirect('teacher_dashboard')
    elif request.user.is_student():
        return redirect('student_dashboard')
    elif request.user.is_parent():
        return redirect('parent_dashboard')
    return redirect('login')

# Dashboards
@login_required
def admin_dashboard(request):
    return render(request, 'authentication/admin_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'authentication/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'authentication/student_dashboard.html')

@login_required
def parent_dashboard(request):
    return render(request, 'authentication/parent_dashboard.html')
