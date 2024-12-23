from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import Analysis

from analysis.analysis.serializers.crud.crud import AnalysisCrudSerializer


class AnalysisUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Analysis.objects.all().select_related(
        'device', 'type'
    )
    serializer_class = AnalysisCrudSerializer
