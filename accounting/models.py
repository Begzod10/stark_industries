from datetime import datetime

from django.db import models

from users.models import User


class PaymentType(models.Model):
    payment_type = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_type


class Payment(models.Model):
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    amount = models.BigIntegerField(default=0)
    date = models.DateField(null=True, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)


class PaymentAnalysis(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    analysis = models.ForeignKey('analysis.Analysis', on_delete=models.SET_NULL, null=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    amount = models.BigIntegerField(default=0)
    date = models.DateField(null=True, default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.BigIntegerField(default=0)
