from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

jobs = ['reception', 'admin', 'operator', 'mainAdmin']


class Job(models.Model):
    name = models.CharField(max_length=255)
    has_client = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_default_jobs(sender, **kwargs):
    for job in jobs:
        if Job.objects.filter(name=job).count() == 0:
            Job.objects.create(name=job)
