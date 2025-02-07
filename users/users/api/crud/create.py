from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from analysis.models import Analysis
from users.models import UserAnalysis
from users.models.user import User, UserRequest
from users.users.serializers.crud.crud import UserCrudSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCrudSerializer


class UseraddRequest(APIView):
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        user = User.objects.get(id=id)
        doctor_id = request.data.get("doctor_id")
        doctor = User.objects.get(id=doctor_id)
        from_date = request.data.get("from_date")
        to_date = request.data.get("to_date")
        date = request.data.get("date")
        analysis = request.data.get("analysis", [])

        user_request = UserRequest.objects.create(
            doctor=doctor,
            patient=user,
            from_date=from_date,
            to_date=to_date,
            date=date
        )

        if analysis:
            for analysis_id in analysis:
                UserAnalysis.objects.create(
                    user=user,
                    analysis=Analysis.objects.get(id=analysis_id),
                    request=user_request,
                    status=False,
                    expected_result=None,
                    result=None
                )

        return Response({"message": "Data successfully updated for user"}, status=status.HTTP_200_OK)
