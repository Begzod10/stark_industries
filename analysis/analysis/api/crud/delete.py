from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from analysis.analysis.serializers.crud.crud import AnalysisCrudSerializer
from analysis.models import Analysis


class AnalysisDestroyView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Analysis.objects.all()
    serializer_class = AnalysisCrudSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "Analysis deleted successfully."}, status=status.HTTP_200_OK)
