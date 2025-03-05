from django.db import models
from students.models import Student, Enrollment
from django.utils import timezone

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True, related_name='attendance_records')
    enrolled_class = models.ForeignKey(Enrollment, on_delete=models.CASCADE,null=True, related_name='attendance_records')
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'date')  # Ensures a student can't have multiple attendance records for the same day

    def __str__(self):
        return f"{self.student.first_name} - {self.date} - {self.status}"
