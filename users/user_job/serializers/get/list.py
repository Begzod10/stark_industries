from rest_framework import serializers

from users.models.job import UserJobs


class UserJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobs
        fields = '__all__'
