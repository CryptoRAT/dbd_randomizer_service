from django.db import models
from django.core import serializers

class Perk(models.Model):
    name = models.CharField(max_length=120)
    owner = models.CharField(max_length=30)
    type = models.CharField(
       max_length=10,
       choices=[("Survivor", "Killer")],  # some list of choices
   )
    image_path = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.type}, {self.owner})"

    def to_json(self):
        return serializers.serialize('json', [self])

