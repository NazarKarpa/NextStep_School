from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from course_and_module_app.models import Module
from tasksmarks_app.mixins import *
from lessons_app.models import Lesson, LessonSchedule, Material



class LessonsListView(LoginRequiredMixin, ListView):
    modul = Lesson
    context_object_name = 'lessons'
    template_name = 'lessons/lesson_list.html'

    def get_queryset(self):
        queryset = Lesson.objects.all()

        return queryset


class LessonsDetailView(LoginRequiredMixin, DetailView, TaskDetailMixins):
    modul = Lesson
    context_object_name = 'lesson'
    template_name = 'lessons/lesson_detail.html'

    def get_queryset(self):
        queryset = Lesson.objects.all()
        return queryset



class MaterialDetail(LoginRequiredMixin, DetailView):
    modul = Material
    context_object_name = 'material'
    template_name = 'lessons/material_detail.html'

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


