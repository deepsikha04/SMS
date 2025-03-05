from django.contrib.auth.models import AbstractUser
from django.db import models

# Extend the default User model
class User(AbstractUser):
    ROLES = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Parent', 'Parent'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='student')

    def is_admin(self):
        return self.role == 'Admin'

    def is_teacher(self):
        return self.role == 'Teacher'

    def is_student(self):
        return self.role == 'Student'

    def is_parent(self):
        return self.role == 'Parent'
