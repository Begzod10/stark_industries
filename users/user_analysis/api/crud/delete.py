from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from users.models.user import User
from users.models.analysis import UserAnalysis, Analysis
from users.models.job import UserJobs
from users.user_analysis.serializers.crud.serializers import UserAnalysisGetSerializer
import pprint


class UserAnalysisDeleteView(generics.GenericAPIView):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserAnalysisGetSerializer

    def delete(self, request, *args, **kwargs):
        pprint.pprint(request.data)
        type_get = request.data.get('type')
        user = request.data.get('user')
        user = User.objects.get(id=user)
        if type_get == "packet":
            packet_id = request.data.get('packet_id')
            analysis = Analysis.objects.filter(packet_id=packet_id).all()
            UserAnalysis.objects.filter(analysis__in=analysis, user=user).delete()
        else:
            analysis_id = request.data.get('analysis_id')
            UserAnalysis.objects.filter(id=analysis_id, user=user).delete()
        exists = UserAnalysis.objects.filter(user=user, paid=False).exists()
        if exists:
            UserJobs.objects.filter(user=user).update(paid=False)
        return Response({"message": "User analysis deleted successfully."}, status=status.HTTP_200_OK)
