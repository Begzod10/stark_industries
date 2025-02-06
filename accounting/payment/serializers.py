from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status

from accounting.models import Payment
from users.models import User, UserAnalysis, UserJobs
import pprint


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        pprint.pprint(validated_data['user_id'])
        user = User.objects.get(id=int(validated_data['user_id']))
        user_jobs = UserJobs.objects.get(user=user)
        payment_sum = 0
        user_analysis = UserAnalysis.objects.filter(user=user, paid=False).all()
        for analysis in user_analysis:
            payment_sum += analysis.analysis.price
            analysis.paid = True
            analysis.save()
        user_jobs.paid = True
        validated_data['amount'] = payment_sum
        return Payment.objects.create(**validated_data)
