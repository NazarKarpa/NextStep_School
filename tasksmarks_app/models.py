from django.contrib.auth.models import User
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
    option = models.ForeignKey(TestTask, on_delete=CASCADE, related_name='answers', verbose_name='Завдання')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'Name" -{self.name},'


class ChoiceTest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_choice', verbose_name='Вибір студента')
    option_choice = models.ForeignKey(Option, on_delete=CASCADE, related_name='option_choices', verbose_name='Вибір тесту')
    choice = models.ForeignKey(TestTask, on_delete=CASCADE, related_name='choice_test', verbose_name='Збереження тесту')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Зробленно в ')


class AnswerTask(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_task', verbose_name='Вибір студента')
    choice = models.ForeignKey(Task, on_delete=CASCADE, related_name='choice_task', verbose_name='Збереження завдання')
    answer = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Зробленно в ')

    def __str__(self):
        return f'student - {self.student}, Task - {self.choice}, answer - {self.answer}'