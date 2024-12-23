from rest_framework import serializers

from job.models import Job


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name']
