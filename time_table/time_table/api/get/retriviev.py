from rest_framework import generics

from job.models import Job
from job.job.serializers.get.retriviev import JobSerializer


class JobRetrieve(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
