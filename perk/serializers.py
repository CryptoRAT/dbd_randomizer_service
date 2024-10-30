from rest_framework import serializers
from .models import Perk

class PerkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perk
        fields = ('name', 'owner', 'type', 'image_path')
        extra_kwargs = {
            'owner': {'required': True},
            'type': {'required': True},
            'image_path': {'required': True},
        }

    # Custom validation for owner
    def validate_owner(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Owner name must be at least 3 characters long.")
        return value

    def validate_type(self, value):
        if value not in ['Survivor', 'Killer']:
            raise serializers.ValidationError("Invalid type. Must be 'Survivor' or 'Killer'.")
        return value

    # Override the update method
    def update(self, instance, validated_data):
        # Ensure that the unique validation doesn't cause issues when updating the same object
        if 'name' in validated_data and instance.name == validated_data['name']:
            validated_data.pop('name')  # Remove name if it's the same as the existing instance

        return super().update(instance, validated_data)
