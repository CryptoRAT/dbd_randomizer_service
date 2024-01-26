from rest_framework import serializers
from .models import Killer


class KillerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Killer
        fields = ('name', 'image_path',)
