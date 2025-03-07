from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import Analysis

from analysis.analysis.serializers.crud.crud import AnalysisCrudSerializer
from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class AnalysisCreateView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Analysis.objects.all().select_related(
        'device', 'type'
    )
    serializer_class = AnalysisCrudSerializer

    def perform_create(self, serializer):
        self.instance = serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        instance = self.instance
        get_serializer = AnalysisGetSerializer(instance)

        return Response(get_serializer.data, status=response.status_code)
