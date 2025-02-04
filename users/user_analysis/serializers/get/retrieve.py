from rest_framework import serializers
from users.models.analysis import UserAnalysis


class UserAnalysisGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysis
        fields = '__all__'
