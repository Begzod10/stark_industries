from django.db import models

from device.models import Device


class Packet(models.Model):
    name = models.CharField(max_length=255)


class AnalysisType(models.Model):
    name = models.CharField(max_length=255)


class Packet(models.Model):
    name = models.CharField(max_length=255)


class Container(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)


class Analysis(models.Model):
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    packet = models.ForeignKey(Packet, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    type = models.ForeignKey(AnalysisType, on_delete=models.SET_NULL, null=True)
    container = models.ForeignKey(Container, on_delete=models.SET_NULL, null=True)
    code_name = models.CharField(max_length=255,null=True)

