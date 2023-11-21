from django.contrib import admin
from .models import Perk

class PerksAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'type', 'image_path')

# Register your models here.

admin.site.register(Perk, PerksAdmin)
