from rest_framework import serializers

from users.models.analysis import UserAnalysis
from users.models.user import UserRequest
from users.models.user import User
import pprint


class UserAnalysisCreateUpdateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    analysis_list = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = UserAnalysis
        fields = ['user', 'analysis_list']

    def create(self, validated_data):
        user = validated_data.pop('user')
        analysis_list = validated_data.pop('analysis_list', [])  # Ensure it exists

        # Create multiple UserAnalysis records
        user_analysis_instances = [
            UserAnalysis.objects.create(user=user, analysis_id=analysis)
            for analysis in analysis_list
        ]

        return user_analysis_instances[0] if user_analysis_instances else None  # Return one instance
