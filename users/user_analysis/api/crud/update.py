from rest_framework import generics

from users.models.analysis import UserAnalysis
from users.user_analysis.serializers.crud.serializers import UserAnalysisCreateUpdateSerializer

class UserAnalysisUpdateView(generics.UpdateAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisCreateUpdateSerializer
