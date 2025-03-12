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
        representation['status'] = ['black', 'green', 'blue'][instance.status]
        for analysis in instance.analysis.all():
            representation['analysis'] = AnalysisSerializer(analysis).data

        return representation

    # def get_analysis_details(self, obj):
    #     # Get name and surname from the user
    #
    #     # Get all related Analysis objects
    #     user_analyses = UserAnalysis.objects.filter(branch=obj.branch).all()
    #
    #     # Create a list of separate dictionaries
    #     result = []
    #     for i, user_analysis in enumerate(user_analyses, len(user_analyses)):
    #         name = user_analysis.user.name if user_analysis.user else None  # Use analysis.user
    #         surname = user_analysis.user.surname if user_analysis.user else None
    #         analysis = user_analysis.analysis.all()
    #         for a in analysis:
    #             analysis_data = AnalysisSerializer(a).data
    #             print(user_analysis.user)
    #
    #             result.append({
    #                 "name": name,
    #                 "surname": surname,
    #                 "analysis": analysis_data
    #             })
    #
    #     return result
