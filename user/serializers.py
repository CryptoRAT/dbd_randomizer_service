# This is the class for serializing the user model
from rest_framework import serializers
from .models import RegisteredUser
from rest_framework import serializers
from django.contrib.auth.models import User  # Assuming you are using Django's built-in User model




class RegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ('email', 'name', 'is_active', 'is_staff',)



class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirmPassword = serializers.CharField(write_only=True)
    displayName = serializers.CharField()

    def validate(self, data):
        # Additional custom validation can be added here
        # For example, checking if passwords match
        if data.get('password') != data.get('confirmPassword'):
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def create(self, validated_data):
        # Custom create method for handling user registration logic
        email = validated_data.get('email')
        password = validated_data.get('password')
        display_name = validated_data.get('displayName')

        # Create a new user using Django's built-in User model
        user = RegisteredUser.objects.create_user(username=display_name, email=email, password=password)

        user.save()
        # TODO: Send a welcome email to the user. This can be done any number of ways.
        # 1. Put the logic here..probably asynchronously.
        # 2. Use Django signals to send an email when a user is created (https://docs.djangoproject.com/en/3.0/topics/signals/)
        # 3. Use a third-party service like SendGrid (https://sendgrid.com/docs/for-developers/sending-email/django/)

        return user
