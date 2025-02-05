from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)
    has_client = models.BooleanField(default=False)
