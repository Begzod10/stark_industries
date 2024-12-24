from rest_framework import serializers

from analysis.models import Analysis, AnalysisType
from device.models import Device


class AnalysisGetSerializer(serializers.ModelSerializer):
    device = serializers.CharField(source='device.name')

    # type = serializers.CharField(source='analysistype.name')

    class Meta:
        model = Analysis
        fields = ['id', 'name', 'device', 'price']
