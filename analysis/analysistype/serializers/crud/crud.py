from rest_framework import serializers
from analysis.models import AnalysisType


class AnalysisTypeCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisType
        fields = ['id', 'name']
