from rest_framework import serializers
from analysis.models import AnalysisType

from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class AnalysisTypeGetSerializer(serializers.ModelSerializer):
    analyses = AnalysisGetSerializer(many=True, read_only=True, source='analysis_set')

    class Meta:
        model = AnalysisType
        fields = ['id', 'name', 'analyses']
