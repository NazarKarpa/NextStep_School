from django.urls import path
from course_and_module_app import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
]

app_name = 'course_and_module_app'
