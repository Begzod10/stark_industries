from rest_framework import serializers

from users.models.analysis import UserAnalysis
from users.models.user import UserRequest
from users.models.user import User


class UserAnalysisCreateUpdateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    request = serializers.PrimaryKeyRelatedField(queryset=UserRequest.objects.all())

    class Meta:
        model = UserAnalysis
        fields = '__all__'
