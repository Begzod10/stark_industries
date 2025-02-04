from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from job.models import Job
from job.jobs.serializers.crud.crud import JobSerializer, DoctorSerializer
from users.models.user import User

from job.jobs.filters.doctor_filter import UserFilter


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class GetDoctorsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
