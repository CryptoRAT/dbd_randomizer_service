from django.contrib import admin
from .models import Killer

class KillerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_path')

# Register your models here.

admin.site.register(Killer, KillerAdmin)
