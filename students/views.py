from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Value, CharField
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Student, Enrollment, AcademicRecord
from .forms import StudentForm, EnrollmentForm, AcademicRecordForm
from classes.models import Class


# ✅ Manage Students (Fixed Search Issue)
def manage_students(request):
    query = request.GET.get('search', '').strip()  # Remove leading/trailing spaces
    students = Student.objects.all()

    if query:
        students = students.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name', output_field=CharField())
        ).filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(contact_number__icontains=query) |
            Q(email__icontains=query) |
            Q(full_name__icontains=query)  # Search Full Name
        )

    return render(request, 'frontend/manage_students.html', {
        'students': students,
        'search_query': query  # Pass query to template for showing search input
    })


# ✅ Add Student
def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        academic_form = AcademicRecordForm(request.POST)

        if student_form.is_valid() and academic_form.is_valid():
            student = student_form.save()
            academic_record = academic_form.save(commit=False)
            academic_record.student = student
            academic_record.save()
            messages.success(request, 'Student added successfully!')
            return redirect('frontend:manage_students')
        else:
            messages.error(request, 'Error adding the student. Please check the form.')
    else:
        student_form = StudentForm()
        academic_form = AcademicRecordForm()

    return render(request, 'frontend/add_student.html', {
        'student_form': student_form,
        'academic_form': academic_form
    })


# ✅ Edit Student (Handles Missing Academic Record)
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    academic_record, created = AcademicRecord.objects.get_or_create(student=student)

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        academic_form = AcademicRecordForm(request.POST, instance=academic_record)

        if student_form.is_valid() and academic_form.is_valid():
            student_form.save()
            academic_form.save()
            messages.success(request, 'Student details updated successfully!')
            return redirect('frontend:manage_students')
        else:
            messages.error(request, 'Error updating the student. Please check the form.')
    else:
        student_form = StudentForm(instance=student)
        academic_form = AcademicRecordForm(instance=academic_record)

    return render(request, 'frontend/edit_student.html', {
        'student_form': student_form,
        'academic_form': academic_form,
        'student': student
    })


# ✅ Delete Student (Handles Dependencies)
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    try:
        student.delete()
        messages.success(request, 'Student deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting student: {e}')
    
    return redirect('frontend:manage_students')


# ✅ Enroll Student (Improved Form Handling)
def enroll_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = student
            enrollment.save()
            messages.success(request, f'{student.first_name} has been enrolled successfully.')
            return redirect('frontend:manage_students')
        else:
            messages.error(request, 'Error enrolling the student. Please check the form.')
    else:
        form = EnrollmentForm()

    classes = Class.objects.all()
    return render(request, 'frontend/enroll_student.html', {
        'form': form,
        'classes': classes,
        'student': student
    })
