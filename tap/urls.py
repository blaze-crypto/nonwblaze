from django.contrib.auth import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterViewSet, CoinViewset,
    BoostViewset, UserBoostViewset,
    TaskViewset, FriendViewset,
    HomeView, TaskView, task_complete,
    BoostView, buy_boost, FriendsView,
    login_view, logout_view, RegistrationView,
)

router = DefaultRouter()

router.register('register', RegisterViewSet)
router.register('coins', CoinViewset)
router.register('boosts', BoostViewset)
router.register('user-boosts', UserBoostViewset)
router.register('tasks', TaskViewset)
router.register('friends', FriendViewset)

urlpatterns = [
    # register
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # my apps
    path('', HomeView.as_view(), name='home'),
    path('task/', TaskView.as_view(), name='task'),
    path('complete-task/<int:task_id>/', task_complete, name='complete-task'),
    path('boost/', BoostView.as_view(), name='boost'),
    path('boost/buy/', buy_boost, name='buy_boost'),
    path('friends/', FriendsView.as_view(), name='friends'),
]

urlpatterns += router.urls
