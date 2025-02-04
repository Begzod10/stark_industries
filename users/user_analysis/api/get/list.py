from rest_framework.generics import ListAPIView

from users.models.analysis import UserAnalysis
from users.user_analysis.serializers.get.retrieve import UserAnalysisGetSerializer


class UsersAnalysisList(ListAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisGetSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = UserAnalysis.objects.filter(user=request['user'])
        return self.get_queryset()
