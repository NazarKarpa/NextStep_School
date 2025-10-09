from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(User, blank=True, related_name='courses_as_students')
    teacher = models.ForeignKey(User, blank=True, on_delete=CASCADE, related_name='courses_as_teacher')

    def __str__(self):
        return f'Course_name- {self.name}'


class Module(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, blank=True, null=True,  on_delete=CASCADE, related_name='course')

    def __str__(self):
        return f'Module_name - {self.name}'


class ModuleSchedule(models.Model):
    start_module = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey(Module, blank = True, on_delete=CASCADE, related_name='moduls')
