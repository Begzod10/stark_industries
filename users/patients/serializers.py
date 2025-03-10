from rest_framework import serializers

from users.models import User, UserJobs


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'phone_number', 'user_id']


class PatientListSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'phone_number', 'user_id', 'deleted', 'age', 'status']

    def get_age(self, obj):
        return obj.calculate_age()

    def get_status(self, obj):
        status = UserJobs.objects.get(user=obj)
        return status.paid
