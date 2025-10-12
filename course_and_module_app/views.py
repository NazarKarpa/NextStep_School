from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from course_and_module_app.models import Course, Module, ModuleSchedule


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course_and_module/course_list.html'

    def get_queryset(self):
        queryset = Course.objects.filter(students = self.request.user).all()

        return queryset

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_and_module/course_page.html'

    # def get_queryset(self):
    #     queryset = ModuleSchedule.objects.filter().all()
    #
    #     return queryset
