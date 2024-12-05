from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=255)


class UserJobs(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
