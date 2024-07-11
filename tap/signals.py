from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Coins


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_coins(sender, instance, created, **kwargs):
    if created:
        Coins.objects.create(user=instance)
