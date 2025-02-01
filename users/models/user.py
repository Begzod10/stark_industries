from django.contrib.auth.models import AbstractUser
from django.db import models
from job.models import Job


class User(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    passport_series = models.CharField(max_length=255, default='')
    passport_number = models.CharField(max_length=255, default='')
    branch = models.ForeignKey('branch.Branch', on_delete=models.CASCADE, default=1)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def jobs(self):
        return Job.objects.filter(userjobs__user=self)


class UserRequest(models.Model):
    doctor = models.ForeignKey(User, related_name='doctor_requests', on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(User, related_name='patient_requests', on_delete=models.SET_NULL, null=True)
    from_date = models.TimeField()
    to_date = models.TimeField()
    date = models.DateField(null=True)
