from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('task/', views.TaskView.as_view(), name='task'),
    path('boost/', views.BoostView.as_view(), name='boost'),
    path('friends/', views.FriendsView.as_view(), name='friends'),
]
