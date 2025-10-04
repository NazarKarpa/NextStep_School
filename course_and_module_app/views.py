from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from course_and_module_app.models import Course, Module


class CourseList(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course_and_module/course_list.html'


class ModuleList(LoginRequiredMixin, ListView):
    model = Module
    context_object_name = 'moduls'
    template_name = 'course_and_module/module_list.html'

