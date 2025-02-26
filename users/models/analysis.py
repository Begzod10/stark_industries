from django.db import models

from users.models.job import UserJobs
from analysis.models import Analysis


class UserAnalysis(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    analysis = models.ManyToManyField(Analysis, related_name='user_analysis')
    request = models.ForeignKey('UserRequest', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    expected_result = models.TextField(null=True)
    paid = models.BooleanField(default=False, null=True)
    payment = models.ForeignKey('accounting.Payment', on_delete=models.SET_NULL, null=True)
    by_packet = models.BooleanField(default=False)
    result = models.TextField(null=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    units = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status and self.paid:
            UserJobs.objects.filter(user=self.user).update(paid=True)
        else:
            UserJobs.objects.filter(user=self.user).update(paid=False)
