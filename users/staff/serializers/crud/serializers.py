from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models.user import User
from job.jobs.serializers.crud.crud import JobSerializer


class StaffSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch',
                  'username', 'email', 'passport_series', 'passport_number']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ushbu username allaqachon ishlatilgan.")
        return value
