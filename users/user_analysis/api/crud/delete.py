from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from users.models.analysis import UserAnalysis
from users.user_analysis.serializers.crud.serializers import UserAnalysisCreateUpdateSerializer


class UserAnalysisDeleteView(generics.DestroyAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisCreateUpdateSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "User analysis deleted successfully."}, status=status.HTTP_200_OK)
