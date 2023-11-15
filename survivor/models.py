from django.db import models

# Create your models here.
class Survivor(models.Model):
    name = models.CharField(max_length=120)
    image_path = models.TextField()

    def _str_(self):
        return self.name