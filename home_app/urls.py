from django.urls import path
from home_app.views import AnnouncementListView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-list')
]