from rest_framework import serializers, viewsets
from rest_framework.serializers import ModelSerializer
from users.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
