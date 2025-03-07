from rest_framework import serializers

from device.models import Device
from users.models.analysis import UserAnalysis


class DeviceRetrieveSerializer(serializers.ModelSerializer):
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = ['id', 'name', 'img','ip_address' ,'branch', 'can_delete']

    def get_can_delete(self, obj):
        can_delete = obj.analysis_set.exists()

        if can_delete:
            return False
        else:
            return True


class UsersDeviceAnalysisSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    name = serializers.CharField(source='user.name')
    surname = serializers.CharField(source='user.surname')
    user_analysis = serializers.IntegerField(source='id')

    class Meta:
        model = UserAnalysis
        fields = ['id', 'name', 'surname', 'user_analysis']


class UserAnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysis
        fields = ['expected_result']
