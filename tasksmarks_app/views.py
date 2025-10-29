from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .mixins import *


class MainTaskView(TaskListMixin, TaskDetailMixins, LoginRequiredMixin, TemplateView):
    template_name = 'task/task_homework.html'


