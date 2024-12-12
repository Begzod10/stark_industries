from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from job.models import Job
from job.jobs.serializers.crud.crud import JobSerializer


class JobDeleteView(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobUpdateView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
