from django.urls import path
from tasksmarks_app import views

urlpatterns = [
    path('lessons/<int:pk>/tasks/', views.LessonTaskListView.as_view(), name='task-list'),


]

app_name = 'task_app'