from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status

from accounting.models import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
