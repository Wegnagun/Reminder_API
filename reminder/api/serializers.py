from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Event

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    # owner = SlugRelatedField(
    #     read_only=True,
    #     slug_field='owner',
    #     default=serializers.CurrentUserDefault
    # )

    class Meta:
        model = Event
        fields = '__all__'
