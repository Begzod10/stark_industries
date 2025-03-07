from rest_framework import generics
from job.models import Job
from job.job.serializers.crud.crud import JobCreateUpdateSerializer


class JobDestroyApiView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = JobCreateUpdateSerializer
    queryset = Job.objects.all()
