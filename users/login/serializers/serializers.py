from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data["user_id"] = user.id
        data["name"] = user.name
        data["surname"] = user.surname
        data['branch'] = user.branch.name
        data['branch_id'] = user.branch.id
        data["role"] = user.userjobs_set.first().job.name if user.userjobs_set.exists() else "No Role"

        data['photo'] = user.photo.url if user.photo else None

        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = RefreshToken(attrs['refresh'])
        user = User.objects.get(id=refresh.payload['user_id'])

        data["message"] = "Token refreshed successfully"
        data["user_id"] = user.id
        data["name"] = user.name
        data["surname"] = user.surname  # Fix overwriting
        data["branch"] = user.branch.name if user.branch else None
        data["branch_id"] = user.branch.id if user.branch else None
        data["role"] = user.userjobs_set.first().job.name if user.userjobs_set.exists() else "No Role"
        data['photo'] = user.photo.url if user.photo else None

        return data
