from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()


class Event(models.Model):
    event_name = models.CharField(max_length=150)
    event_date = models.DateField()
    event_type = models.CharField(max_length=150,
                                  choices=settings.EVENT_CHOICES,
                                  default='Nothing')
    event_text = models.TextField()
    event_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event'
    )

    def __str__(self):
        return self.event_name
