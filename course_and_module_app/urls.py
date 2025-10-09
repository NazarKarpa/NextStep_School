from django.urls import path
from course_and_module_app import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course-list'),
    path('<int:pk>/', views.ModuleList.as_view(), name='module-list')
]

app_name = 'course_and_module_app'
