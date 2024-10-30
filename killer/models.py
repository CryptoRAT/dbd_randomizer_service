from django.db import models
from django.core import serializers

class Killer(models.Model):
    name = models.CharField(max_length=120)
    image_path = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.image_path})"

    def to_json(self):
        return serializers.serialize('json', [self])