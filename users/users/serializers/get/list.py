from rest_framework import serializers
from users.models.user import User
from branch.models import Branch
from users.models.user import UserRequest
from analysis.models import Analysis
from users.models.analysis import UserAnalysis
from rest_framework import serializers


# class UserGetSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = [
#             'name', 'surname', 'username', ''
#         ]
#
#
