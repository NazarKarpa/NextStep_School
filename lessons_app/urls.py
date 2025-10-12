from django.urls import path
from lessons_app import views

urlpatterns = [
    path('', views.LessonsListView.as_view(), name='lessons-list'),
    path('<int:pk>/', views.LessonsDetailView.as_view(), name='lesson-detail'),
]

app_name = 'lessons_app'
