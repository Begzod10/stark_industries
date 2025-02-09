from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models.user import User
from job.jobs.serializers.crud.crud import JobSerializer
from django.db.models import Q


class StaffSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'birth_date', 'phone_number', 'address', 'sex', 'branch',
                  'username', 'email', 'passport_series', 'passport_number']

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password('12345678')
        user.save()
        return user

    def validate_username(self, value):
        if self.instance is not None:
            if User.objects.filter(username=value).filter(~Q(id=self.instance.id)).exists():
                raise serializers.ValidationError("Ushbu username allaqachon ishlatilgan.")
        else:
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("Ushbu username allaqachon ishlatilgan.")
        return value


class StaffSerializerPassword(ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
