from rest_framework import serializers

from accounting.models import PaymentType
from branch.models import Branch
from .models import Overhead, OverheadType


class OverheadTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverheadType
        fields = ['id', 'name', 'order']





class OverheadSerializer(serializers.ModelSerializer):
    payment = serializers.CharField(source='payment.payment_type',read_only=True)
    payment_id = serializers.PrimaryKeyRelatedField(
        queryset=PaymentType.objects.all(),
        source='payment',
        write_only=True
    )
    branch = serializers.CharField(source='branch.name',read_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(),
        source='branch',
        write_only=True
    )
    type = serializers.CharField(source='type.name',read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=OverheadType.objects.all(),
        source='type',
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Overhead
        fields = ['id', 'name', 'payment', 'payment_id', 'created', 'price',
                  'branch', 'branch_id', 'type', 'type_id', 'deleted']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not ret['name'] and instance.type:
            ret['name'] = instance.type.name
        return ret
