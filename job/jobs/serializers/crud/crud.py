from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from job.models import Job
from users.models.user import User


class JobSerializer(ModelSerializer):
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id', 'name', 'has_client', 'can_delete']

    def get_can_delete(self, obj):
        jobs = ['admin', 'doctor', 'patient', 'reception']
        if obj.name in jobs:
            return False
        else:
            return True


class DoctorSerializer(ModelSerializer):
    jobs = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'username', 'jobs']

    def get_jobs(self, obj):
        return [{"id": job.id, "name": job.name} for job in obj.jobs.all()]
