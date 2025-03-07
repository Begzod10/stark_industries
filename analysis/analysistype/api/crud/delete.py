from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from analysis.analysistype.serializers.crud.crud import AnalysisTypeCrudSerializer
from analysis.models import AnalysisType


class AnalysisTypeDestroyView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = AnalysisType.objects.all()
    serializer_class = AnalysisTypeCrudSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Analysis Type deleted successfully."}, status=status.HTTP_200_OK)
