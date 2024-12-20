from rest_framework import serializers

from users.models.user import UserRequest

from users.models.user import User
from calendars.models import Calendar


class UserRequestCreateUpdateSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    calendar = serializers.PrimaryKeyRelatedField(queryset=Calendar.objects.all())

    class Meta:
        model = UserRequest
        fields = '__all__'
