from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'department', 'phone']
