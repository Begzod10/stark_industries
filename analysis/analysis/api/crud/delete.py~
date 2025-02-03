from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import Analysis

from analysis.analysis.serializers.crud.crud import AnalysisCrudSerializer


class AnalysisDestroyView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Analysis.objects.all()
    serializer_class = AnalysisCrudSerializer
