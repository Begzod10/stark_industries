from django.db import models

from analysis.models import Analysis
from users.models.job import UserJobs


class UserAnalysis(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    analysis = models.ForeignKey(Analysis, on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey('UserRequest', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    expected_result = models.TextField(null=True)
    result = models.TextField(null=True)
    paid = models.BooleanField(default=False, null=True)
    payment = models.ForeignKey('accounting.Payment', on_delete=models.SET_NULL, null=True)
    by_packet = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        super(UserAnalysis, self).save(*args, **kwargs)
        if self.status and self.paid and self.result:
            UserJobs.objects.filter(user=self.user).update(paid=True)
        else:
            UserJobs.objects.filter(user=self.user).update(paid=False)
