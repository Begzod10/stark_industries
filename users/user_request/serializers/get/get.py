from rest_framework import serializers
from users.models.user import UserRequest
from datetime import datetime
from users.models.job import UserJobs


class UserRequestSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    patient_name = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = UserRequest
        fields = ['id', 'doctor', 'patient_name', 'start', 'end', 'date', 'status']

    def get_start(self, obj):
        return f"{obj.date} {obj.from_date.strftime('%H:%M')}"

    def get_end(self, obj):
        return f"{obj.date} {obj.to_date.strftime('%H:%M')}"

    def get_patient_name(self, obj):
        if obj.patient:
            return f"{obj.patient.name} {obj.patient.surname}"
        return None

    def get_status(self, obj):
        if obj.patient:
            user_jobs = UserJobs.objects.filter(user=obj.patient)
            if user_jobs.exists():
                return user_jobs.first().paid
        return False
