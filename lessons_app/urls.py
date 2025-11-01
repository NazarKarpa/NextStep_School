from django.urls import path
from lessons_app import views

urlpatterns = [
    path('lessons-list', views.LessonsListView.as_view(), name='lessons-list'),
    path('<int:pk>/', views.LessonsDetailView.as_view(), name='lesson-detail'),
    path('material/<int:pk>/', views.MaterialDetail.as_view(), name='material-detail'),
]

app_name = 'lessons_app'
