from django.shortcuts import render
from .models import Student, Teacher, Transaction
from django.db.models import Count
from datetime import datetime

# Report for student performance (based on book transactions)
def student_performance_report(request):
    students = Student.objects.all()
    report_data = []

    for student in students:
        # Counting the number of books a student has borrowed
        borrowed_books = Transaction.objects.filter(borrower=student.user).count()
        report_data.append({
            'student': student,
            'borrowed_books': borrowed_books
        })

    return render(request, 'frontend/student_performance_report.html', {'report_data': report_data})

# Report for student attendance (assuming attendance is stored in a related model or a separate table)
def student_attendance_report(request):
    # Example placeholder data for attendance report
    students = Student.objects.all()
    report_data = []

    for student in students:
        # Dummy attendance data (replace with actual data logic)
        attendance_percentage = 85  # Placeholder value
        report_data.append({
            'student': student,
            'attendance_percentage': attendance_percentage
        })

    return render(request, 'frontend/student_attendance_report.html', {'report_data': report_data})

# Report for class schedule (assuming class schedules are available or a placeholder for now)
def class_schedule_report(request):
    teachers = Teacher.objects.all()
    report_data = []

    for teacher in teachers:
        # Dummy class schedule data (replace with actual data)
        schedule = 'Math - Monday, Physics - Wednesday'  # Placeholder value
        report_data.append({
            'teacher': teacher,
            'schedule': schedule
        })

    return render(request, 'frontend/schedule_report.html', {'report_data': report_data})
