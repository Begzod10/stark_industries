from django.db import models


class DeviceBrand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True, default=1)
    ip_address = models.CharField()
    port = models.IntegerField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=50, default="PSWD")
    protocol_version = models.CharField(max_length=20, default="E1394-97")
    receiver_name = models.CharField(max_length=100, default="LIS")
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    brand = models.ForeignKey(DeviceBrand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
