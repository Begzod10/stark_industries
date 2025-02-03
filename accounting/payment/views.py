from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from accounting.models import Payment
from accounting.payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
