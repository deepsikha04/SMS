from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm
from students.models import Student
from django.db.models import Count

@login_required
def mark_attendance(request):
    # Ensure we are only passing students with complete data
    students = Student.objects.exclude(first_name__isnull=True, last_name__isnull=True)

    # Ensure student objects exist before passing them to the template
    student_data = []
    for student in students:
        if student.first_name and student.last_name:  # Check that first_name and last_name are not None or empty
            student_data.append(student)

    form = AttendanceForm()
    
    # Render the attendance marking page with the filtered students
    return render(request, 'frontend/mark_attendance.html', {'students': student_data, 'form': form})

@login_required
def attendance_list(request):
    attendance_records = Attendance.objects.all().order_by('-date')
    return render(request, 'frontend/attendance_list.html', {'attendance_records': attendance_records})

@login_required
def attendance_report(request):
    report = Attendance.objects.values('student__first_name', 'student__last_name', 'status').annotate(count=Count('status'))
    return render(request, 'frontend/attendance_report.html', {'report': report})
