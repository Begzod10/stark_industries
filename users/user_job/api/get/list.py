from rest_framework import generics

from users.models.user import User
from analysis.analysis.serializers.get.get import AnalysisGetSerializer


class AnalysisListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AnalysisGetSerializer
