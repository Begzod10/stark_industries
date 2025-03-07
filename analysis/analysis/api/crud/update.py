from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from analysis.models import Analysis

from analysis.analysis.serializers.crud.crud import AnalysisCrudSerializer

from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class AnalysisUpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Analysis.objects.all()
    serializer_class = AnalysisCrudSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        get_serializer = AnalysisGetSerializer(instance)
        return Response(get_serializer.data, status=response.status_code)
