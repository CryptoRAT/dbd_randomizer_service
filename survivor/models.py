from django.db import models


class Survivor(models.Model):
    name = models.CharField(max_length=120)
    image_path = models.TextField()

    def _str_(self):
        return self.name