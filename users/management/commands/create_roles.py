# authentication/management/commands/create_roles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from users.models import User  # Import your custom User model

class Command(BaseCommand):
    help = 'Create roles and assign permissions for the School Management System'

    def handle(self, *args, **kwargs):
        # Define roles (groups)
        roles = ['Admin', 'Teacher', 'Student', 'Parent']

        # Create roles (groups)
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            self.stdout.write(f'Role "{role}" {"created" if created else "already exists"}.')

        # Assign permissions to roles based on school management needs
        admin_group = Group.objects.get(name='Admin')
        teacher_group = Group.objects.get(name='Teacher')
        student_group = Group.objects.get(name='Student')
        parent_group = Group.objects.get(name='Parent')

        # Define permissions (example permissions related to the school system)
        content_type = ContentType.objects.get_for_model(User)  # Adjust to your relevant model
        permissions = [
            ('add_student', 'Can add student'),  # Admin/Teacher
            ('view_student', 'Can view student'),  # Admin/Teacher/Parent
            ('change_student', 'Can change student details'),  # Admin/Teacher
            ('delete_student', 'Can delete student'),  # Admin
            ('view_grades', 'Can view grades'),  # Teacher/Parent/Student
            ('change_grades', 'Can change grades'),  # Teacher
            ('view_attendance', 'Can view attendance'),  # Admin/Teacher/Parent/Student
            ('mark_attendance', 'Can mark attendance'),  # Teacher
        ]

        # Create permissions dynamically
        for codename, name in permissions:
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type
            )
            self.stdout.write(f'Permission "{name}" {"created" if created else "already exists"}.')

        # Assign permissions to groups
        admin_group.permissions.set(Permission.objects.filter(codename__in=[
            'add_student', 'view_student', 'change_student', 'delete_student', 'view_grades', 'view_attendance'
        ]))

        teacher_group.permissions.set(Permission.objects.filter(codename__in=[
            'add_student', 'view_student', 'change_student', 'view_grades', 'change_grades', 'view_attendance', 'mark_attendance'
        ]))

        student_group.permissions.set(Permission.objects.filter(codename__in=[
            'view_grades', 'view_attendance'
        ]))

        parent_group.permissions.set(Permission.objects.filter(codename__in=[
            'view_student', 'view_grades', 'view_attendance'
        ]))

        self.stdout.write(self.style.SUCCESS('Roles and permissions for the School Management System created successfully.'))
