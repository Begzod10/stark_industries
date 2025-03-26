from rest_framework.serializers import ModelSerializer, ListSerializer
from rest_framework import serializers
from users.models import UserAnalysis
from analysis.analysis.serializers.get.get import AnalysisSerializer


class LaboratoryAnalysisSerializer(ModelSerializer):
    class Meta:
        model = UserAnalysis
        # fields = ['date', 'target', 'paid', 'status', 'user', 'name', 'surname', 'urgent', 'id', 'analysis',
        #           'container', 'by_packet', 'code', 'start_branch', 'end_branch']
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.user.name
        representation['surname'] = instance.user.surname
        representation['start_branch'] = instance.branch.name
        representation['end_branch'] = instance.branch.name
        representation['status'] = ['black', 'green', 'blue'][instance.status - 1]
        representation['isChecked'] = True if instance.status == 2 else False
        for analysis in instance.analysis.all():
            representation['analysis'] = AnalysisSerializer(analysis).data

        return representation


class LaboratoryUpdateSerializer(ModelSerializer):
    analysis = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserAnalysis
        fields = "__all__"

    def update(self, instance, validated_data):
        # Toggle status between 2 and 3
        instance.status = 2 if instance.status == 3 else 3
        instance.save()

        return instance  # ✅ Return the instance instead of a dictionary

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = instance.user.name
        representation['surname'] = instance.user.surname
        representation['start_branch'] = instance.branch.name
        representation['end_branch'] = instance.branch.name
        representation['status'] = ['black', 'green', 'blue'][instance.status - 1]
        representation['isChecked'] = True if instance.status == 2 else False
        for analysis in instance.analysis.all():
            representation['analysis'] = AnalysisSerializer(analysis).data

        return representation
