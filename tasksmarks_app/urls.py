from django.urls import path
from tasksmarks_app import views

urlpatterns = [
    path('lessons/<int:pk>/tasks/', views.LessonTaskListView.as_view(), name='task-list'),
    path('api/check-test/<int:test_id>/', views.check_test, name='check-test'),


]

app_name = 'task_app'