from tkinter.constants import CASCADE

from django.db import models
import course_and_module_app.models as module

class Lesson(models.Model):
    name = models.CharField(max_length=150)
    material = models.TextField()
    modul = models.ForeignKey(module.Module, on_delete=CASCADE, related_name='Lessons')

    def __str__(self):
        return f'Lesson_name - {self.name}, modul - {self.modul}'
