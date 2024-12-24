from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import AnalysisType

from analysis.analysistype.serializers.get.get import AnalysisTypeGetSerializer


class AnalysisTypeListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = AnalysisType.objects.all()
    serializer_class = AnalysisTypeGetSerializer
