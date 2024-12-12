from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from users.models.job import UserJobs
from users.user_job.serializers.crud.serializers import UserJobsSerializer


class UserJobsDelete(generics.DestroyAPIView):
    queryset = UserJobs.objects.all()
    serializer_class = UserJobsSerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "UserJobs deleted successfully."}, status=status.HTTP_200_OK)
