from django.contrib import admin
from .models import UserBoost, Coins, Boosts, Tasks, TasksTypes, Friends


class AdminCoins(admin.ModelAdmin):
    list_display = ('id', 'coin_user', 'coins', 'coins_level')
    search_fields = ('coin_user',)
    list_filter = ('coin_user', 'coins_level')


class AdminBoosts(admin.ModelAdmin):
    list_display = ('id', 'boost_title', 'boost_price')
    search_fields = ('boost_title',)
    list_filter = ('boost_title',)


class AdminTasks(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_description', 'task_price')
    search_fields = ('task_title', 'task_description')
    list_filter = ('task_title', 'task_description')


class AdminUserBoost(admin.ModelAdmin):
    list_display = ('id', 'user', 'level')
    search_fields = ('user',)
    list_filter = ('user', 'level')


class AdminTasksTypes(admin.ModelAdmin):
    list_display = ('id', 'type_title')
    search_fields = ('type_title',)
    list_filter = ('type_title',)


class AdminFriends(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(UserBoost, AdminUserBoost)
admin.site.register(Coins, AdminCoins)
admin.site.register(Boosts, AdminBoosts)
admin.site.register(Tasks, AdminTasks)
admin.site.register(TasksTypes, AdminTasksTypes)
admin.site.register(Friends, AdminFriends)
