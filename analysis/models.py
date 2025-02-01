from django.db import models

from device.models import Device


class Packet(models.Model):
    name = models.CharField(max_length=255)


class AnalysisType(models.Model):
    name = models.CharField(max_length=255)


class Analysis(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    packet = models.ForeignKey(Packet, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    type = models.ForeignKey(AnalysisType, on_delete=models.SET_NULL, null=True)
