from django.db import models
from users.models import User
from classes.models import Class
from django.utils.timezone import now

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile',null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, default="0000000000")
    email = models.EmailField(unique=True)
    subjects_taught = models.CharField(max_length=255, default="Not Assigned")

    date_of_hire = models.DateField(default=now) 
    availability = models.JSONField(blank=True, null=True)  # Store availability as JSON data

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ClassAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='class_assignments')
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='teacher_assignments')
    assigned_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('teacher', 'assigned_class')  # Ensures a teacher is not assigned twice to the same class

    def __str__(self):
        return f"{self.teacher.first_name} assigned to {self.assigned_class.class_name}"

class TeacherSchedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schedules')
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=9, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                                           ('Thursday', 'Thursday'), ('Friday', 'Friday')])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.teacher.first_name} - {self.class_instance.class_name} on {self.day_of_week}"
