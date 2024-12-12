from rest_framework import serializers
from users.models.user import User


class UserCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'phone_number', 'address', 'sex']
