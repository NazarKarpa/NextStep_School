from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .mixins import *
import tasksmarks_app.models
from lessons_app.models import Lesson
from tasksmarks_app.forms import *
from django.shortcuts import get_object_or_404

class LessonTaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'

    def get_queryset(self):
        lesson = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
        return lesson.tasks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
        return context



class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/task_homework.html'







