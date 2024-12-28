from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models.user import User
from job.jobs.serializers.crud.crud import JobSerializer


class StaffSerializerGet(ModelSerializer):
    job = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch',
                  'username', 'email', 'passport_series', 'passport_number', 'job']

    def get_job(self, obj):
        job = obj.userjobs_set.first()
        if job:
            return job.job.name
