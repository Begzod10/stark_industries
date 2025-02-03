from rest_framework import serializers

from accounting.models import PaymentAnalysis


class PaymentAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAnalysis
        fields = '__all__'
