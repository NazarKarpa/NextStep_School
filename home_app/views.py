from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from home_app.models import Announcement

class AnnouncementListView(ListView):
    model = Announcement
    context_object_name = 'announcements'
    template_name = 'home/announcement_list.html'
