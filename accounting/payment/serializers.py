from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from accounting.payment_types.serializers.retrieve import PaymentTypeRetrieveSerializer
from accounting.models import Payment
from users.models import UserAnalysis, UserJobs
from rest_framework.response import Response

from rest_framework import status


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_type', 'amount', 'date', 'user', 'branch']

    def create(self, validated_data):
        user = validated_data['user']
        payment_type = validated_data['payment_type']
        branch = validated_data['branch']

        user_jobs = UserJobs.objects.get(user=user)
        analysis_list = validated_data.pop('analysis_list')
        payment_sum = 0
        user_analysis = UserAnalysis.objects.filter(user=user, analysis__in=analysis_list).all()
        payment = Payment.objects.create(user=user, payment_type=payment_type, branch=branch)
        for analysis in user_analysis:
            payment_sum += analysis.analysis.price
            analysis.paid = True
            analysis.payment = payment
            analysis.save()

        user_jobs.paid = True
        user_jobs.save()
        payment.amount = payment_sum
        payment.save()
        return Response({"message": "Payment created successfully.", "payment": PaymentSerializer(payment).data},
                        status=status.HTTP_200_OK)


class PaymentListSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()
    # amount = serializers.SerializerMethodField()
    payment_type = PaymentTypeRetrieveSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'payment_type', 'date', 'user', 'amount', 'branch', 'deleted']

    def get_user(self, obj):
        return f"{obj.user.name} {obj.user.surname}"

    # def get_amount(self, obj):
    #     return UserAnalysis.objects.filter(payment=obj).aggregate(amount=Sum('analysis__price'))
