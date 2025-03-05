from django.db import models
from django.conf import settings  # Use settings to get the custom User model
from students.models import Student  # Import from the students app

# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# Exam Model
class Exam(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()  # Example: 2 hours
    max_marks = models.PositiveIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Corrected

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

# Student Exam Enrollment
class StudentExam(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Use existing student model
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.name}"

# Grade Model
class Grade(models.Model):
    student_exam = models.OneToOneField(StudentExam, on_delete=models.CASCADE, null=True)
    marks_obtained = models.PositiveIntegerField(null=True)
    grade = models.CharField(max_length=2, blank=True, null=True)

    def calculate_grade(self):
        percentage = (self.marks_obtained / self.student_exam.exam.max_marks) * 100
        if percentage >= 90:
            self.grade = 'A+'
        elif percentage >= 80:
            self.grade = 'A'
        elif percentage >= 70:
            self.grade = 'B'
        elif percentage >= 60:
            self.grade = 'C'
        elif percentage >= 50:
            self.grade = 'D'
        else:
            self.grade = 'F'
        self.save()

    def save(self, *args, **kwargs):
        self.calculate_grade()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_exam.student.user.username} - {self.grade}"
