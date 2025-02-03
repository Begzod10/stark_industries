from rest_framework import generics

from job.models import Job
from job.job.serializers.get.list import JobListSerializer


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
