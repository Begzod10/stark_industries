from django.db import models

class AnalysisType(models.Model):
    name = models.CharField(max_length=255)


class Device(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True)
    ip_address = models.GenericIPAddressField()


class Analysis(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    type = models.ForeignKey(AnalysisType, on_delete=models.SET_NULL, null=True)


class UserAnalysis(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    analysis = models.ForeignKey(Analysis, on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey('UserRequest', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    expected_result = models.TextField()
    result = models.TextField()
