from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True)
    ip_address = models.GenericIPAddressField()
