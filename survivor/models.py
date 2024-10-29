from django.db import models


class Survivor(models.Model):
    name = models.CharField(max_length=120)
    image_path = models.TextField()

    def __str__(self):
        return self.name