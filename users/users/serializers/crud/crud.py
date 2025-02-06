from rest_framework import serializers
from users.models.user import User
from branch.models import Branch
from users.models.user import UserRequest
from analysis.models import Analysis
from users.models.analysis import UserAnalysis
from rest_framework import serializers


class UserCrudSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, write_only=True)
    from_date = serializers.TimeField(required=False, write_only=True)
    to_date = serializers.TimeField(required=False, write_only=True)
    date = serializers.DateField(required=False, write_only=True)
    analysis = serializers.PrimaryKeyRelatedField(queryset=Analysis.objects.all(), required=False, write_only=True,
                                                  many=True)
    email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch', 'username',
            'email', 'passport_series', 'passport_number', 'doctor_id', 'from_date', 'to_date', 'date', 'analysis'
        ]

    def create(self, validated_data):
        return self._save_user(None, validated_data)

    def update(self, instance, validated_data):
        return self._save_user(instance, validated_data)

    def _save_user(self, instance, validated_data):
        doctor = validated_data.pop('doctor_id', None)
        from_date = validated_data.pop('from_date', None)
        to_date = validated_data.pop('to_date', None)
        date = validated_data.pop('date', None)
        analysis = validated_data.pop('analysis', None)

        if instance is None:
            instance = User.objects.create(**validated_data)
        else:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

        user_request = UserRequest.objects.filter(patient=instance).first()

        if doctor and from_date and to_date and date:
            if user_request:
                user_request.doctor = doctor
                user_request.from_date = from_date
                user_request.to_date = to_date
                user_request.date = date
                user_request.save()
            else:
                user_request = UserRequest.objects.create(
                    doctor=doctor,
                    patient=instance,
                    from_date=from_date,
                    to_date=to_date,
                    date=date
                )

        if user_request and analysis:
            UserAnalysis.objects.filter(user=instance, request=user_request).delete()
            for analysis_item in analysis:
                UserAnalysis.objects.create(
                    user=instance,
                    analysis=analysis_item,
                    request=user_request,
                    status=False,
                    expected_result=None,
                    result=None
                )

        return instance

# class UserCrudSerializer(serializers.ModelSerializer):
#     branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
#     doctor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, write_only=True)
#     from_date = serializers.TimeField(required=False, write_only=True)
#     to_date = serializers.TimeField(required=False, write_only=True)
#     date = serializers.DateField(required=False, write_only=True)
#     analysis_id = serializers.PrimaryKeyRelatedField(queryset=Analysis.objects.all(), required=False, write_only=True,
#                                                      many=True)
#     email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
#
#     class Meta:
#         model = User
#         fields = [
#             'name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch', 'username',
#             'email', 'passport_series', 'passport_number', 'doctor_id', 'from_date', 'to_date', 'date', 'analysis_id'
#         ]
#
#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError("Ushbu username allaqachon ishlatilgan.")
#         return value
#
#     def create(self, validated_data):
#         doctor = validated_data.pop('doctor_id', None)
#         from_date = validated_data.pop('from_date', None)
#         to_date = validated_data.pop('to_date', None)
#         date = validated_data.pop('date', None)
#         analysis = validated_data.pop('analysis_id', None)  # Bu endi list bo'ladi
#         user = User.objects.create(**validated_data)
#
#         user_request = None
#         if doctor and from_date and to_date and date:
#             user_request = UserRequest.objects.create(
#                 doctor=doctor,
#                 patient=user,
#                 from_date=from_date,
#                 to_date=to_date,
#                 date=date
#             )
#
#         if user_request and analysis:
#             for analysis_item in analysis:
#                 UserAnalysis.objects.create(
#                     user=user,
#                     analysis=analysis_item,
#                     request=user_request,
#                     status=False,
#                     expected_result=None,
#                     result=None
#                 )
#         return user
#
#
# class UpdateUserCrudSerializer(serializers.ModelSerializer):
#     branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
#     doctor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, write_only=True)
#     from_date = serializers.TimeField(required=False, write_only=True)
#     to_date = serializers.TimeField(required=False, write_only=True)
#     date = serializers.DateField(required=False, write_only=True)
#     analysis_id = serializers.PrimaryKeyRelatedField(queryset=Analysis.objects.all(), required=False, write_only=True, many=True)
#     email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
#
#     class Meta:
#         model = User
#         fields = [
#             'name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch', 'username',
#             'email', 'passport_series', 'passport_number', 'doctor_id', 'from_date', 'to_date', 'date', 'analysis_id'
#         ]
#
#     def validate_username(self, value):
#         if User.objects.filter(username=value).exclude(id=self.instance.id).exists():
#             raise serializers.ValidationError("Ushbu username allaqachon ishlatilgan.")
#         return value
#
#     def update(self, instance, validated_data):
#         doctor = validated_data.pop('doctor_id', None)
#         from_date = validated_data.pop('from_date', None)
#         to_date = validated_data.pop('to_date', None)
#         date = validated_data.pop('date', None)
#         analysis = validated_data.pop('analysis_id', None)
#
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#
#         user_request = UserRequest.objects.filter(patient=instance).first()
#         if doctor and from_date and to_date and date:
#             if user_request:
#                 user_request.doctor = doctor
#                 user_request.from_date = from_date
#                 user_request.to_date = to_date
#                 user_request.date = date
#                 user_request.save()
#             else:
#                 user_request = UserRequest.objects.create(
#                     doctor=doctor,
#                     patient=instance,
#                     from_date=from_date,
#                     to_date=to_date,
#                     date=date
#                 )
#
#         if user_request and analysis:
#             UserAnalysis.objects.filter(user=instance, request=user_request).delete()
#             for analysis_item in analysis:
#                 UserAnalysis.objects.create(
#                     user=instance,
#                     analysis=analysis_item,
#                     request=user_request,
#                     status=False,
#                     expected_result=None,
#                     result=None
#                 )
#
#         return instance
