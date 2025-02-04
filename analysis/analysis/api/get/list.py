from rest_framework import generics

from analysis.models import Analysis
from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class AnalysisListView(generics.ListAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisGetSerializer
