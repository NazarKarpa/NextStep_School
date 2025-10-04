from django.db import models
from django.db.models import CASCADE
import course_and_module_app.models as module

class Material(models.Model):
    link = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)


class Lesson(models.Model):
    name = models.CharField(max_length=150)
    modul = models.ForeignKey(module.Module, on_delete=CASCADE, related_name='Lessons')
    material = models.ManyToManyField(Material, blank=True, related_name = 'materials')

    def __str__(self):
        return f'Lesson_name - {self.name}, modul - {self.modul}'


class LessonSchedule(models.Model):
    start_lessons = models.DateTimeField(blank=True, null=True)
    lesson = models.ForeignKey(Lesson, blank=True, on_delete=CASCADE, related_name='lesson')
