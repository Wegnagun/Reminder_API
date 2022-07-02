from django.db import models
from django.conf import settings


class Owner(models.Model):
    nickname = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nickname}'


class Birthday(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    type = models.CharField(max_length=150,
                            choices=settings.EVENT_CHOICES)
    text = models.TextField()
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='event'
    )

    def __str__(self):
        return self.name
