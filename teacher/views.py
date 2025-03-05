from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, TeacherSchedule
from .forms import TeacherForm

# 1️⃣ List all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'frontend/teacher_list.html', {'teachers': teachers})


# 2️⃣ Add a new teacher
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'frontend/add_teacher.html', {'form': form})

# 3️⃣ View teacher details
def teacher_detail(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)
    return render(request, 'frontend/teacher_detail.html', {'teachers': teachers})

# 4️⃣ Edit teacher details
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'frontend/edit_teacher.html', {'form': form})

# 5️⃣ Delete a teacher
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'frontend/delete_teacher.html', {'teacher': teacher})

# 6️⃣ View teacher schedules
def teacher_schedule(request):
    schedules = TeacherSchedule.objects.all().select_related('teacher', 'class_instance')
    return render(request, 'frontend/teacher_schedule.html', {'schedules': schedules})
