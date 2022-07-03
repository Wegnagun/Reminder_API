from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Birthday(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='birthday'
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    type = models.CharField(max_length=150,
                            choices=settings.EVENT_CHOICES)
    text = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event'
    )

    def __str__(self):
        return self.name
