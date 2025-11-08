from django import forms
from tasksmarks_app.models import *

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['name', 'description', 'status']
#
#     def __init__(self, *args, **kwargs):
#         super(TaskForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control'})
