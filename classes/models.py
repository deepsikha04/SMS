from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.class_name

class ClassSchedule(models.Model):
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                                          ('Thursday', 'Thursday'), ('Friday', 'Friday')])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
         return f"{self.class_instance.class_name}"
