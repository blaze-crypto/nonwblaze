from rest_framework import serializers
from django.contrib.auth.models import User
from tap.models import Coins, Tasks, Boosts, UserBoost


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.save()
        return user


class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = '__all__'


class GetCoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = ('coin_user', 'coins_level', 'coins')


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class GetTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('task_title', 'task_description', 'task_price')


class BoostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boosts
        fields = '__all__'


class GetBoostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boosts
        fields = ('boost_title', 'boost_price')


class UserBoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBoost
        fields = '__all__'


class GetUserBoostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBoost
        fields = ('user', 'boost', 'level')
