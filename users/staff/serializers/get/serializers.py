from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models.user import User
from job.jobs.serializers.crud.crud import JobSerializer
import datetime


class StaffSerializerGet(ModelSerializer):
    job = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch',
                  'username', 'email', 'passport_series', 'passport_number', 'job', 'age','photo']

    def get_job(self, obj):
        job = obj.userjobs_set.first()
        if job:
            return job.job.name

    def get_age(self, obj):
        now = datetime.datetime.now()
        age = now.year - obj.birth_date.year
        return age
