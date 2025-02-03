from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from job.models import Job
from job.job.serializers.crud.crud import JobCreateUpdateSerializer


class JobCreateApiView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = JobCreateUpdateSerializer
    queryset = Job.objects.all()
