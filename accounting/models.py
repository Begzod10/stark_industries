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


class BranchItems(models.Model):
    # Define size choices as a tuple of (value, label) pairs
    # bu variantlar ozgartiriladi
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    size = models.CharField(max_length=255, choices=SIZE_CHOICES, default='M')  # Added choices
    count = models.BigIntegerField(default=0)


class BranchOverhead(models.Model):
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    price = models.BigIntegerField(default=0)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    branch_item = models.ForeignKey(BranchItems, on_delete=models.SET_NULL, null=True)
    count = models.BigIntegerField(default=0)
    date = models.DateField(null=True, default=datetime.now)