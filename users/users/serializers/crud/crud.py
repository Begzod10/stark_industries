from django.db.models import Sum
from rest_framework import serializers
from datetime import timedelta
from datetime import datetime

from analysis.models import Analysis
from branch.models import Branch
from users.models.analysis import UserAnalysis
from users.models.job import UserJobs, Job
from users.models.user import User
from users.models.user import UserRequest


class UserCrudSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, write_only=True)
    from_date = serializers.TimeField(required=False, write_only=True)
    to_date = serializers.TimeField(required=False, write_only=True)
    date = serializers.DateField(required=False, write_only=True)
    user_request_id = serializers.IntegerField(required=False, write_only=True)
    email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
    photo = serializers.ImageField(required=False, allow_null=True)
    password = serializers.CharField(required=False)
    analysis_list = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    packet_list = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = User
        fields = [
            'name', 'surname', 'birth_date', 'phone_number', 'address', 'password', 'sex', 'branch', 'username',
            'email', 'passport_series', 'passport_number', 'doctor_id', 'from_date', 'to_date', 'date',
            'user_request_id', 'photo'
            , 'analysis_list', 'packet_list'
        ]

    def create(self, validated_data):
        return self._save_user(None, validated_data)

    def update(self, instance, validated_data):
        return self._save_user(instance, validated_data)

    def _save_user(self, instance, validated_data):
        user_request = None

        name = validated_data.pop('name', None)
        surname = validated_data.pop('surname', None)
        birth_date = validated_data.pop('birth_date', None)
        phone_number = validated_data.pop('phone_number', None)
        address = validated_data.pop('address', None)
        sex = validated_data.pop('sex', None)
        branch = validated_data.pop('branch', None)
        username = validated_data.pop('username', None)
        email = validated_data.pop('email', None)
        passport_series = validated_data.pop('passport_series', None)
        passport_number = validated_data.pop('passport_number', None)

        user_request_id = validated_data.pop('user_request_id', None)
        doctor = validated_data.pop('doctor_id', None)
        from_date = validated_data.pop('from_date', None)
        to_date = validated_data.pop('to_date', None)
        date = validated_data.pop('date', None)

        job = Job.objects.filter(name="patient").first()
        password = "12345678"

        if instance is None:
            instance = User.objects.create(name=name,
                                           surname=surname,
                                           birth_date=birth_date,
                                           phone_number=phone_number,
                                           address=address,
                                           password=password,
                                           sex=sex,
                                           branch=branch,
                                           username=username,
                                           email=email,
                                           passport_series=passport_series,
                                           passport_number=passport_number)
            if password is not None:
                instance.set_password(password)
                instance.save()
            UserJobs.objects.create(user=instance, job=job)
        else:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            if user_request_id:
                user_request = UserRequest.objects.filter(id=user_request_id, patient=instance).first()

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

        if user_request:
            user_analysis, created = UserAnalysis.objects.get_or_create(user=instance, request=user_request)

            analysis_list = validated_data.pop('analysis_list', [])
            packet_list = validated_data.pop('packet_list', [])

            user_analysis.analysis.set(analysis_list + packet_list)

            total_price = Analysis.objects.filter(id__in=analysis_list + packet_list).aggregate(Sum('price'))[
                              'price__sum'] or 0

            user_analysis.price = total_price
            user_analysis.by_packet = bool(packet_list)
            user_analysis.save()

        return instance
