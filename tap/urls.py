from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('coins', views.CoinViewset)
router.register('boosts', views.BoostViewset)
router.register('user-boosts', views.UserBoostViewset)
router.register('tasks', views.TaskViewset)
router.register('friends', views.FriendViewset)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('task/', views.TaskView.as_view(), name='task'),
    path('complete-task/<int:task_id>/', views.task_complete, name='complete-task'),
    path('boost/', views.BoostView.as_view(), name='boost'),
    path('boost/buy/', views.buy_boost, name='buy_boost'),
    path('friends/', views.FriendsView.as_view(), name='friends'),
]

urlpatterns += router.urls
