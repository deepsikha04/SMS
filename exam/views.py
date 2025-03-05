from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Exam, StudentExam, Grade
from .forms import ExamForm, GradeForm
from students.models import Student

# View to manage exams
@method_decorator(login_required, name='dispatch')
class ExamListView(View):
    def get(self, request):
        exams = Exam.objects.all()
        return render(request, 'frontend/exam_list.html', {'exams': exams})

# View to add/edit an exam
@method_decorator(login_required, name='dispatch')
class ExamCreateView(View):
    def get(self, request):
        form = ExamForm()
        return render(request, 'frontend/exam_form.html', {'form': form})

    def post(self, request):
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
        return render(request, 'frontend/exam_form.html', {'form': form})

# View to input grades
@method_decorator(login_required, name='dispatch')
class GradeInputView(View):
    def get(self, request, exam_id):
        exam = Exam.objects.get(id=exam_id)
        student_exams = StudentExam.objects.filter(exam=exam)
        return render(request, 'frontend/grade_input.html', {'exam': exam, 'student_exams': student_exams})

    def post(self, request, exam_id):
        exam = Exam.objects.get(id=exam_id)
        student_exams = StudentExam.objects.filter(exam=exam)
        for student_exam in student_exams:
            marks_obtained = request.POST.get(f"marks_{student_exam.id}")
            if marks_obtained:
                grade_instance, created = Grade.objects.get_or_create(student_exam=student_exam)
                grade_instance.marks_obtained = marks_obtained
                grade_instance.save()
        return redirect('exam_list')

# View to generate report card for a student
@method_decorator(login_required, name='dispatch')
class ReportCardView(View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        student_exams = StudentExam.objects.filter(student=student)
        grades = Grade.objects.filter(student_exam__in=student_exams)
        return render(request, 'frontend/report_card.html', {'student': student, 'grades': grades})
