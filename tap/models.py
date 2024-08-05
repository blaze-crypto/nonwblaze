from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self):
        return f'{self.user} - {self.friends.count()} friends'

    class Meta:
        db_table = 'friends'
        verbose_name = 'Friends'
        verbose_name_plural = 'Friends'


class Coins(models.Model):
    coin_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    coins_level = models.IntegerField(default=1, null=True, blank=True)
    coins = models.IntegerField(default=0, null=True, blank=True)
    energy_level = models.IntegerField(default=1000, null=True, blank=True)
    speed_recharge = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return f'{self.coin_user} - {self.coins} coins'

    class Meta:
        db_table = 'coins'
        verbose_name = 'Coins'
        verbose_name_plural = 'Coins'


class TasksTypes(models.Model):
    type_title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.type_title

    class Meta:
        db_table = 'tasks_types'
        verbose_name = 'Task Type'
        verbose_name_plural = 'Task Types'


class Tasks(models.Model):
    tasks_type = models.ForeignKey(TasksTypes, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=255, null=True, blank=True)
    tasks_icon = models.ImageField(upload_to='tasks_icon/', null=True, blank=True)
    task_description = models.TextField(null=True, blank=True)
    task_price = models.IntegerField(null=True, blank=True)
    task_url = models.URLField(null=True, blank=True)
    task_active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.task_title

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Boosts(models.Model):
    boost_title = models.CharField(max_length=255, null=True, blank=True)
    boost_icon = models.ImageField(upload_to='boost_icons/', null=True, blank=True)
    boost_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.boost_title

    class Meta:
        db_table = 'boosts'
        verbose_name = 'Boost'
        verbose_name_plural = 'Boosts'


class UserBoost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boosts, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} - {self.boost.boost_title} (Level {self.level})'

    class Meta:
        db_table = 'user_boosts'
        verbose_name = 'User Boost'
        verbose_name_plural = 'User Boosts'
