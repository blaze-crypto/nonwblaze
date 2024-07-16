from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from rest_framework import viewsets
from .models import Coins, Tasks, Boosts, UserBoost, TasksTypes, Friends
from .serializers import (CoinsSerializer, GetCoinsSerializer,
                          TasksSerializer, GetTasksSerializer,
                          BoostsSerializer, GetBoostsSerializer,
                          UserBoostSerializer, GetUserBoostsSerializer)


class CoinViewset(viewsets.ModelViewSet):
    queryset = Coins.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CoinsSerializer
        return GetCoinsSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TasksSerializer
        return GetTasksSerializer


class BoostViewset(viewsets.ModelViewSet):
    queryset = Boosts.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BoostsSerializer
        return GetBoostsSerializer


class UserBoostViewset(viewsets.ModelViewSet):
    queryset = UserBoost.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserBoostSerializer
        return GetUserBoostsSerializer


class HomeView(TemplateView):
    template_name = 'home.html'
    queryset = Coins.objects.all()


class TaskView(ListView):
    template_name = 'task.html'

    def get_queryset(self):
        return Tasks.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_types = TasksTypes.objects.all()
        tasks_by_type = {}
        for task_type in task_types:
            tasks_by_type[task_type.type_title] = Tasks.objects.filter(tasks_type=task_type)
        context['task_types'] = task_types
        context['tasks_by_type'] = tasks_by_type
        return context


@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    user_coins, created = Coins.objects.get_or_create(coin_user=request.user)
    user_coins.coins += task.task_price
    user_coins.save()
    task.task_active = False
    task.save()
    return redirect(task.task_url)


class FriendsView(ListView):
    template_name = 'friend.html'
    context_object_name = 'friends_list'

    def get_queryset(self):
        user = self.request.user
        try:
            friend_instance = Friends.objects.get(user=user)
            friends = friend_instance.friends.all()
        except Friends.DoesNotExist:
            friends = []
        return friends

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friends = context['friends_list']
        invite_links = [
            f"https://t.me/tap_blaze_bot?start=invite_{friend.id}"
            for friend in friends
        ]
        context['friends'] = zip(friends, invite_links)
        return context


class BoostView(ListView):
    template_name = 'boost.html'
    context_object_name = 'boosts_list'

    def get_queryset(self):
        return Boosts.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get current user and user's boosts and levels
        user = self.request.user
        user_boosts = UserBoost.objects.filter(user=user)
        user_boost_levels = {boost.boost.id: boost.level for boost in user_boosts}

        # Add boosts and user_boost_levels to the context
        context['boosts'] = self.get_queryset()
        context['user_boost_levels'] = user_boost_levels

        return context


@login_required
def buy_boost(request):
    if request.method == 'POST':
        boost_id = request.POST.get('boost_id')
        try:
            boost = Boosts.objects.get(id=boost_id)
        except Boosts.DoesNotExist:
            messages.error(request, "Boost does not exist.")
            return redirect('boost')
        user = request.user
        try:
            user_profile = Coins.objects.get(user=user)
        except Coins.DoesNotExist:
            messages.error(request, "User profile not found.")
            return redirect('boost')
        user_coins = user_profile.coins
        if user_coins >= boost.price:
            user_profile.coins -= boost.price
            user_profile.save()
            user_boost, created = UserBoost.objects.get_or_create(user=user, boost=boost)
            boost.price *= 2
            boost.save()
            user_boost.level += 1
            user_boost.save()

            messages.success(request, f"You have successfully upgraded {boost.name}!")
        else:
            messages.error(request, "Insufficient coins to buy this boost.")

        return redirect('boost')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('boost')
