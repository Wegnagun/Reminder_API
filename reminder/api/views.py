from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Birthday, Event
from .serializers import BirthdaySerializer, EventSerializer, UserSerializer

User = get_user_model()


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BirthdayViewSet(viewsets.ModelViewSet):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
