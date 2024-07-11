from django.shortcuts import get_object_or_404
from .models import UserBoost, Boosts


def add_boosts_to_user(user, boost_ids):
    user_boosts = []
    for boost_id in boost_ids:
        boost = get_object_or_404(Boosts, id=boost_id)
        user_boost, created = UserBoost.objects.get_or_create(user=user, boost=boost)

        if not created:
            user_boost.level += 1
            user_boost.save()

        user_boosts.append(user_boost)

    return user_boosts
