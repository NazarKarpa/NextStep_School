from django.urls import path
from tasksmarks_app import views

urlpatterns = [
    path('lessons/<int:pk>/tasks/', views.LessonTaskListView.as_view(), name='task-list'),
    path('lessons/<int:pk>/tasks/<int:lesson_id>/', views.TaskDetailView.as_view(), name='task-detail'),

]

app_name = 'task_app'