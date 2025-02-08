from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from users.models import UserAnalysis
from users.models.user import UserRequest
from users.user_request.serializers.crud.serializers import UserRequestCreateUpdateSerializer


class UserRequestDeleteView(generics.DestroyAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestCreateUpdateSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "UserJobs deleted successfully."}, status=status.HTTP_200_OK)


class UserRequestAnalysisDeleteView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        user_request_id = request.query_params.get("user_request_id")

        user_request = UserRequest.objects.filter(id=user_request_id).first()

        UserAnalysis.objects.filter(request=user_request).delete()

        user_request.delete()

        return Response({"message": "UserRequest va unga tegishli analysislar o‘chirildi!"},
                        status=status.HTTP_204_NO_CONTENT)
