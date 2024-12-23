from rest_framework import serializers

from job.models import Job


class JobCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name']
