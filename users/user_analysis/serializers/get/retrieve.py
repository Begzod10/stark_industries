from rest_framework import serializers
from users.models.analysis import UserAnalysis
from analysis.analysis.serializers.get.get import AnalysisSerializer


class UserAnalysisGetSerializer(serializers.ModelSerializer):
    analysis = AnalysisSerializer(many=True)  # Use nested serializer
    price = serializers.SerializerMethodField()  # Add price field.

    class Meta:
        model = UserAnalysis
        fields = ['id', 'user', 'analysis', 'status', 'expected_result', 'paid', 'price', 'by_packet']

    def get_price(self, obj):
        total_price = 0
        for analysis in obj.analysis.all():
            total_price += analysis.price
        return total_price
