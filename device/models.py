from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True,default=1)
    ip_address = models.GenericIPAddressField()
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    deleted = models.BooleanField(default=False)
