from datetime import time

from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    starts = models.TimeField()
    ends = models.TimeField()
    phone_number = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    main = models.BooleanField()

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_default_branch(sender, **kwargs):
    if Location.objects.count() == 0:
        Location.objects.create(name="Default Location")
    if Branch.objects.count() == 0:
        location = Location.objects.first()
        if location:
            Branch.objects.create(
                name="Default Branch",
                location=location,
                starts=time(9, 0),
                ends=time(18, 0),
                phone_number="1234567890",
                ip_address="192.168.1.1",
                main=True
            )
