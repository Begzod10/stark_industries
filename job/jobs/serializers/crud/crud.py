from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from job.models import Job
from users.models.user import User


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    jobs = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'username', 'jobs']

    def get_jobs(self, obj):
        return [{"id": job.id, "name": job.name} for job in obj.jobs.all()]
