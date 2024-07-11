from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class TaskView(TemplateView):
    template_name = 'task.html'


class FriendsView(TemplateView):
    template_name = 'friend.html'


class BoostView(TemplateView):
    template_name = 'boost.html'
