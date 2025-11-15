from django import forms
from tasksmarks_app.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user_answer']

    user_answer = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Введіть вашу відповідь тут...',
            'maxlength': '2000'
        }),
        label='Ваша відповідь',
        required=True,
        max_length=2000
    )
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
