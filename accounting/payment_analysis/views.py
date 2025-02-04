from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounting.models import PaymentAnalysis
from accounting.payment_analysis.serializers import PaymentAnalysisSerializer


class PaymentAnalysisViewSet(ModelViewSet):
    queryset = PaymentAnalysis.objects.all()
    serializer_class = PaymentAnalysisSerializer
