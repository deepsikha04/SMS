from django.db import models
from django.conf import settings  # Import settings for AUTH_USER_MODEL
from library.models import Book  # Adjust this import based on where the Book model is located

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='report_student')
    student_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.get_full_name()

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='report_teacher')
    teacher_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.get_full_name()

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='report_transaction_set')  # Unique related_name
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='report_transaction_set')  # Unique related_name
    issued_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.borrower.username}"
