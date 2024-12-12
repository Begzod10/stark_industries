from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import AnalysisType

from analysis.analysistype.serializers.crud.crud import AnalysisTypeCrudSerializer


class AnalysisTypeDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AnalysisType.objects.all().select_related(
        'device', 'type'
    )
    serializer_class = AnalysisTypeCrudSerializer
