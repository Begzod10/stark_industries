from django.db import models

from job.models import Job


class UserJobs(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
