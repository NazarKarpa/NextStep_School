from django.urls import path
from tasksmarks_app import views

urlpatterns = [
    path('lessons/<int:pk>/tasks', views.LessonTaskView.as_view(), name='task_detail'),

]

app_name = 'task_app'