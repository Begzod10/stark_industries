from rest_framework import serializers

from users.models.user import UserRequest

from users.models.user import User


class UserRequestCreateUpdateSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = UserRequest
        fields = ['id', 'doctor', 'patient', 'from_date', 'to_date', 'date']
