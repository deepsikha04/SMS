from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Class, ClassSchedule
from .forms import ClassForm, ClassScheduleForm
from students.models import Enrollment  # To check if the student is already enrolled


# 1️⃣ Admin: Create a new class
@login_required
def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes:manage_classes')  # Redirect to the manage classes page
    else:
        form = ClassForm()
    return render(request, 'frontend/create_class.html', {'form': form})


# 2️⃣ Admin: Create a class schedule
@login_required
def create_class_schedule(request):
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes:manage_classes')
    else:
        form = ClassScheduleForm()
    return render(request, 'frontend/create_class_schedule.html', {'form': form})


# 3️⃣ Admin: Manage all classes and schedules
@login_required
def manage_classes(request):
    classes = Class.objects.all()
    schedules = ClassSchedule.objects.all()
    return render(request, 'frontend/manage_classes.html', {'classes': classes, 'schedules': schedules})


# 4️⃣ Student: View available classes
def view_classes(request):
    classes = Class.objects.all()
    return render(request, 'frontend/view_classes.html', {'classes': classes})


# 5️⃣ Student: Enroll in a class
@login_required
def enroll_in_class(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)

    # Check if the class is already full
    if class_instance.capacity <= class_instance.enrollments.count():
        return render(request, 'frontend/class_full.html', {'class': class_instance})

    # Check if the student is already enrolled
    if Enrollment.objects.filter(student=request.user.student, enrolled_class=class_instance).exists():
        return render(request, 'frontend/already_enrolled.html', {'class': class_instance})

    Enrollment.objects.create(student=request.user.student, enrolled_class=class_instance)
    return redirect('view_classes')


# 6️⃣ Student: View class schedule
def view_class_schedule(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    schedules = ClassSchedule.objects.filter(class_instance=class_instance)
    return render(request, 'frontend/view_class_schedule.html', {'class': class_instance, 'schedules': schedules})
