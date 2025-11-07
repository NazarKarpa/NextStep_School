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

class LessonTaskView(TaskListMixin, TaskDetailMixins, LoginRequiredMixin, TemplateView):
    template_name = 'task/task_homework.html'

    def get_lesson_context(self, ):
        lesson = Lesson.objects.all()
        context = {}
        context.update(self.get_task_list_context())
        for i in lesson:
            context.update(self.get_task_detail_context(task_id=i.id))
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_form'] = TaskForm()
        context.update(self.get_lesson_context())
        return context




