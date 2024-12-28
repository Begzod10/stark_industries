import pprint

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from users.models.user import User
from users.models.job import UserJobs, Job
from users.staff.serializers.crud.serializers import StaffSerializer


class StaffRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        job = Job.objects.get(id=request.data['job_id'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        UserJobs.objects.create(user=serializer.instance, job=job)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
