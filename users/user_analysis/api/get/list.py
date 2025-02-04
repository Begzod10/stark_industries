from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from users.models.analysis import UserAnalysis
from users.user_analysis.serializers.get.retrieve import UserAnalysisGetSerializer
import pprint


class UsersAnalysisList(ListAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisGetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Apply filters properly
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  # Return as Response
