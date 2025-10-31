from django.urls import path
from tasksmarks_app import views

urlpatterns = [
    path('', views.MainTaskView.as_view(), name='task_dashboard'),
    path('<int:pk>/', views.MainTaskView.as_view(), name='task_detail'),

]

app_name = 'task_app'