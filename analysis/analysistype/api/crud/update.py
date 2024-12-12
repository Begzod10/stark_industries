from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import AnalysisType

from analysis.analysistype.serializers.crud.crud import AnalysisTypeCrudSerializer


class AnalysisTypeUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AnalysisType.objects.all()
    serializer_class = AnalysisTypeCrudSerializer
