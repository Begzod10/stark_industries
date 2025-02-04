from django.db import models
from analysis.models import Analysis


class UserAnalysis(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    analysis = models.ForeignKey(Analysis, on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey('UserRequest', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    expected_result = models.TextField(null=True)
    result = models.TextField(null=True)
    paid = models.BooleanField(default=False)


