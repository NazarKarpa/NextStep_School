from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .mixins import *
import tasksmarks_app.models
from lessons_app.models import Lesson
from tasksmarks_app.forms import *
from django.shortcuts import get_object_or_404

from .serializers import ChoiceTestSerializer


class LessonTaskListView(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task_list.html'

    def get_queryset(self):
        lesson = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
        return lesson.tasks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
        test_task = get_object_or_404(TestTask, pk=self.kwargs.get('pk'))
        context['lesson'] = lesson
        context['tasks'] = context['lesson'].tasks.all()
        context['test_task'] = context['lesson'].tasks_test.all()
        context['answer_task_form'] = AnswerTaskForm()
        answer = ChoiceTest.objects.filter(choice=test_task, student=self.request.user).first()
        if answer:
            context['user_answer'] = answer
        return context


    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        test_question_id  = request.POST.get('test_question_id')
        if task_id:
            answer_task_form = AnswerTaskForm(request.POST)

            if answer_task_form.is_valid():
                task = get_object_or_404(Task, pk=task_id)
                answer_task = answer_task_form.save(commit=False)
                answer_task.student = request.user
                answer_task.choice = task
                answer_task.save()
                return redirect('task_app:task-list', pk=kwargs['pk'])

        if test_question_id:
            test = get_object_or_404(TestTask, pk=test_question_id)
            answer_id = request.POST.get('answers')
            option = get_object_or_404(Option, pk=answer_id)

            ChoiceTest.objects.create(student=self.request.user,
                                      option_choice=option,
                                      choice=test)

            return redirect('task_app:task-list', pk=kwargs['pk'])


@api_view(['POST'])
def check_test(request, test_id):
    option_choice_id = request.data.get('option_choice_id')
    option = Option.objects.get(id=option_choice_id)

    is_correct = option.is_correct

    ChoiceTest.objects.create(
        student=request.user,
        option_choice=option,
        choice_id=test_id
    )

    return Response({'is_correct': is_correct})





# class TaskDetailView(DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'task/task_homework.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         lesson = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
#         context['lesson'] = lesson
#         context['tasks'] = context['lesson'].tasks.all()
#         return context







