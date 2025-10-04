from django.contrib import admin
from course_and_module_app import models

admin.site.register(models.Module)
admin.site.register(models.Course)
admin.site.register(models.ModuleSchedule)

