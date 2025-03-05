from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, AcademicRecord
from .forms import StudentForm, AcademicRecordForm

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "academics/student_list.html", {"students": students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "academics/student_detail.html", {"student": student})

@login_required
def add_academic_record(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = AcademicRecordForm(request.POST)
        if form.is_valid():
            academic_record = form.save(commit=False)
            academic_record.student = student
            academic_record.created_by = request.user
            academic_record.save()
            return redirect("student_detail", pk=student.id)
    else:
        form = AcademicRecordForm()
    return render(request, "academics/add_academic_record.html", {"form": form, "student": student})
