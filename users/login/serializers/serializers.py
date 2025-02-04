from rest_framework import serializers

from users.models.job import UserJobs
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print(attrs.get("username"))
        print(attrs.get("password"))
        username_field = get_user_model().USERNAME_FIELD  # Check if it's username or email
        credentials = {username_field: attrs.get("username"), "password": attrs.get("password")}

        user = authenticate(**credentials)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data = super().validate(attrs)
        data['role'] = getattr(user, 'role', None)
        data['name'] = getattr(user, 'name', None)
        data['surname'] = getattr(user, 'surname', None)
        return data
