from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)


class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    starts = models.TimeField()
    ends = models.TimeField()
    phone_number = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    main = models.BooleanField()
