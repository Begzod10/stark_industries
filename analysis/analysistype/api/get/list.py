from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import AnalysisType

from analysis.analysistype.serializers.get.get import AnalysisTypeGetSerializer

from analysis.analysistype.serializers.crud.crud import AnalysisTypeCrudSerializer


class AnalysisTypeListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = AnalysisType.objects.all()
    serializer_class = AnalysisTypeGetSerializer

    def get_serializer_class(self):
        serializer_type = self.request.query_params.get('type', 'get')

        if serializer_type == 'analysis_type':
            return AnalysisTypeCrudSerializer
        return AnalysisTypeGetSerializer
