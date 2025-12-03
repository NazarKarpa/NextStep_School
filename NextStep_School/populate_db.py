from django.contrib.auth.models import User
from tasksmarks_app.models import ChoiceTest, AnswerTask

# Видалити всі відповіді на тести
ChoiceTest.objects.all().delete()