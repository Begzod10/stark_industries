from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserRequest(models.Model):
    doctor = models.ForeignKey(User,  related_name='doctor_requests', on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(User, related_name='patient_requests' ,on_delete=models.SET_NULL, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    calendar = models.ForeignKey('Calendar', on_delete=models.SET_NULL, null=True)
