from rest_framework import generics

from job.models import Job
from job.jobs.serializers.crud.crud import JobSerializer


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
