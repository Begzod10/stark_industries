from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from accounting.models import PaymentType
from accounting.models import Payment
from accounting.payment.serializers import PaymentSerializer, PaymentListSerializer
from users.models import UserAnalysis


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        analyis = UserAnalysis.objects.filter(payment=instance).all()
        for analyis in analyis:
            analyis.paid = False
            analyis.payment = None
            analyis.save()
        return Response({"message": "Payment deleted successfully."}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        payment_type = request.data.get('payment_type')
        payment_type = PaymentType.objects.get(id=payment_type)
        instance = self.get_object()
        instance.payment_type = payment_type
        instance.save()
        return Response({"message": "Payment type updated successfully."}, status=status.HTTP_200_OK)


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    filterset_fields = ['branch', 'payment_type', 'deleted']


class PaymentListUser(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    filterset_fields = ['branch']

    def get_queryset(self):
        if 'pk' not in self.kwargs or getattr(self, 'swagger_fake_view', False):
            return Payment.objects.none()
        user = self.kwargs['pk']
        return Payment.objects.filter(user=user)
