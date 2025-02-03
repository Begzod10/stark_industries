from rest_framework import viewsets
from accounting.models import PaymentType
from accounting.payment_types.serializers.retrieve import PaymentTypeRetrieveSerializer


class PaymentTypeRetrieveViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeRetrieveSerializer
