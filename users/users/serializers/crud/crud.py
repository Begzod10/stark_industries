from rest_framework import serializers
from users.models.user import User
from branch.models import Branch


class UserCrudSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())

    class Meta:
        model = User
        fields = ['name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch', 'username',
                  'email', 'passport_series', 'passport_number']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ushbu username allaqachon ishlatilgan.")
        return value
