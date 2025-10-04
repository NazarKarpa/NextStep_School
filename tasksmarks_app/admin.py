from django.contrib import admin
from tasksmarks_app import models

admin.site.register(models.Task)
admin.site.register(models.TestTask)
admin.site.register(models.Option)
admin.site.register(models.ChoiceTest)
admin.site.register(models.ChoiceTask)
