from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(User, blank=True, related_name='courses_as_students')
    teacher = models.ForeignKey(User, blank=True, on_delete=CASCADE, related_name='courses_as_teacher')

    def __str__(self):
        return f'Course_name- {self.name}'

class Module(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Module_name - {self.name}'