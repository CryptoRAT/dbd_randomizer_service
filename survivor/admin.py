from django.contrib import admin
from .models import Survivor

class SurvivorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_path')

# Register your models here.

admin.site.register(Survivor, SurvivorAdmin)
