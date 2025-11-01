from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .mixins import *
import tasksmarks_app.models

class LessonTaskView(TaskListMixin, TaskDetailMixins, LoginRequiredMixin, TemplateView):
    template_name = 'task/task_homework.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_task_list_context())
        context.update(self.get_task_detail_context(task_id=self.kwargs.get('pk', None)))
        return context




