from django.db import models


class TimeTable(models.Model):
    name = models.CharField(max_length=255)
