from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Coins(models.Model):
    coin_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    coins = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.coin_user} - {self.coins} coins'

    class Meta:
        db_table = 'coins'
        verbose_name = 'Coins'
        verbose_name_plural = 'Coins'


class Tasks(models.Model):
    task_title = models.CharField(max_length=255, null=True, blank=True)
    task_description = models.TextField(null=True, blank=True)
    task_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.task_title

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Boosts(models.Model):
    boost_title = models.CharField(max_length=255, null=True, blank=True)
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
