from rest_framework import serializers
from . models import Event


class UniqueEventValidator:
    def __init__(self, *fields):
        self.fields = fields

    def __call__(self, data):
        query = Event.objects.all()
        for i in query:
            if data[i] in query:
                return serializers.ValidationError("Есть совпадение! (^_-)")
