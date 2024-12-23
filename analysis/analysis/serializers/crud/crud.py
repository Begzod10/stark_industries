from rest_framework import serializers

from analysis.models import Analysis, AnalysisType
from device.models import Device


class AnalysisCrudSerializer(serializers.ModelSerializer):
    device = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=AnalysisType.objects.all())

    class Meta:
        model = Analysis
        fields = ['id', 'name', 'device', 'price', 'type']
