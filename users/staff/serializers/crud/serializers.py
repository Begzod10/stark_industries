from rest_framework.serializers import ModelSerializer

from users.models.user import User
from job.jobs.serializers.crud.crud import JobSerializer


class StaffSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch',
                  'username', 'email', 'passport_series', 'passport_number']

