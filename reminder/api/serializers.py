from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Birthday, Event

User = get_user_model()


class BirthdaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Birthday
        fields = ('name', 'date', 'owner')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    birthday = serializers.StringRelatedField(
        many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'birthday')
