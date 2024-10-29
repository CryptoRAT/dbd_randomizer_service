from django.db import models


class Killer(models.Model):
    name = models.CharField(max_length=120)
    image_path = models.TextField()

    def ___self___(self):
        return self.name