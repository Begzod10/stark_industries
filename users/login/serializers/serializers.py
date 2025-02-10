from rest_framework import serializers

from users.models.job import UserJobs
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)  # Get the default token response

        # Add extra fields to the response
        user = self.user
        data["user_id"] = user.id
        data["name"] = user.name
        data["surname"] = user.surname
        data['branch'] = user.branch.name
        data['branch_id'] = user.branch.id
        data["role"] = user.userjobs_set.first().job.name if user.userjobs_set.exists() else "No Role"
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)  # Get the default token response

        # Add extra fields
        refresh = RefreshToken(attrs['refresh'])
        user = User.objects.get(id=refresh.payload['user_id'])  # Fetch user

        # Add extra fields
        data["message"] = "Token refreshed successfully"
        data["user_id"] = user.id
        data["name"] = user.name
        data["surname"] = user.surname  # Fix overwriting
        data["branch"] = user.branch.name if user.branch else None
        data["branch_id"] = user.branch.id if user.branch else None
        data["role"] = user.userjobs_set.first().job.name if user.userjobs_set.exists() else "No Role"

        return data
