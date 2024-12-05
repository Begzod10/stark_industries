from django.db import models

class Calendar(models.Model):
    date = models.DateField()