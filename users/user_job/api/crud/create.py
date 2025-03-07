from rest_framework import generics

from users.models.job import UserJobs
from users.user_job.serializers.crud.serializers import UserJobsSerializer


class UserJobsCreateView(generics.CreateAPIView):
    queryset = UserJobs.objects.all()
    serializer_class = UserJobsSerializer
