from rest_framework import serializers

from users.models.analysis import UserAnalysis
from users.models.job import UserJobs
import pprint


class UserAnalysisCreateUpdateSerializer(serializers.ModelSerializer):
    analysis_list = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    packet_list = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = UserAnalysis
        fields = ['user', 'analysis_list', 'packet_list']

    def create(self, validated_data):
        user = validated_data.pop('user')
        analysis_list = validated_data.pop('analysis_list', [])  # Ensure it exists
        packet_list = validated_data.pop('packet_list', [])  # Ensure it exists
        UserJobs.objects.filter(user=user).update(paid=False)
        # Create multiple UserAnalysis records
        user_analysis_instances = [
            UserAnalysis.objects.create(user=user, analysis_id=analysis, by_packet=False, branch=user.branch)
            for analysis in analysis_list
        ]
        user_analysis_instances = [
            UserAnalysis.objects.create(user=user, analysis_id=analysis, by_packet=True, branch=user.branch)
            for analysis in packet_list
        ]

        return {"message": "User analysis records created successfully"}


class UserAnalysisGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysis
        fields = ['id', 'user', 'analysis', 'status', 'expected_result', 'result', 'paid', 'price', 'by_packet']
