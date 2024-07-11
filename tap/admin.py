from django.contrib import admin
from .models import UserBoost, Coins, Boosts, Tasks


class AdminCoins(admin.ModelAdmin):
    list_display = ('id', 'user', 'coins')
    search_fields = ('user',)
    list_filter = ('user',)


class AdminBoosts(admin.ModelAdmin):
    list_display = ('id', 'boost_title', 'boost_price')


admin.site.register(UserBoost)
admin.site.register(Coins)
admin.site.register(Boosts)
admin.site.register(Tasks)
