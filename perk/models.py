from django.db import models

# Create your models here.
class Perk(models.Model):
    name = models.CharField(max_length=120)
    owner = models.CharField(max_length=30)
    type = models.CharField(
       max_length=10,
       choices=[("Survivor", "Killer")],  # some list of choices
   )
    image_path = models.TextField()

    def _str_(self):
        return self.name