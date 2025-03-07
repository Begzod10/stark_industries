from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounting.models import PaymentType


class PaymentTypeRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'
