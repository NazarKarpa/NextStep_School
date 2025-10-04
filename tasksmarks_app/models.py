from django.db import models
from django.db.models import CASCADE


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('un_check', 'Un check'),
        ('well', 'Well Done!'),
        ('wrong', 'Wrong, try again')
    ]
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return f'Name - {self.name}, status - {self.status}'


class TestTask(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('well', 'Well Done!'),
        ('wrong', 'Wrong, try again')
    ]
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return f'Name - {self.name}, status - {self.status}'

class Option(models.Model):
    name = models.CharField(max_length=100, verbose_name='Варіант')
    option = models.ForeignKey(TestTask, on_delete=CASCADE, related_name='answers', verbose_name='Вибір варіанту')

    def __str__(self):
        return f'Name" -{self.name},'