from rest_framework import serializers
from users.models.user import UserRequest


class UserRequestSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = UserRequest
        fields = ['doctor', 'patient_name', 'start', 'end', 'date']

    def get_start(self, obj):
        return f"{obj.date} {obj.from_date}"

    def get_end(self, obj):
        return f"{obj.date} {obj.to_date}"

    def get_patient_name(self, obj):
        if obj.patient:
            return f"{obj.patient.name} {obj.patient.surname}"
        return None
