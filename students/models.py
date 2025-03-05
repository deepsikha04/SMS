from django.db import models
from users.models import User
from classes.models import Class

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)  # Enforced non-nullable
    last_name = models.CharField(max_length=100, blank=False, null=False)  # Enforced non-nullable
    dob = models.DateField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    enrollment_date = models.DateField(auto_now_add=True)
    guardian = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AcademicRecord(models.Model):
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True, related_name='academic_record')
    grades = models.JSONField(blank=True, null=True)  # Store grades as JSON data
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Academic Record of {self.student.first_name} {self.student.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='enrollments')
    enrolled_class = models.ForeignKey('classes.Class', on_delete=models.SET_NULL, null=True, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'enrolled_class')  # Ensures a student can't enroll in the same class multiple times

    def __str__(self):
        return f"{self.student.first_name} enrolled in {self.enrolled_class.class_name}"
