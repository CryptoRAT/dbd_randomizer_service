from rest_framework import serializers
from .models import Perk

class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = ('name', 'owner', 'type', 'image_path',)