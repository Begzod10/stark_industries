from django.db import models

from device.models import Device


class AnalysisType(models.Model):
    name = models.CharField(max_length=255)


class Analysis(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    type = models.ForeignKey(AnalysisType, on_delete=models.SET_NULL, null=True)
