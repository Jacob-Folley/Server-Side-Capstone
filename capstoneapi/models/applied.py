from django.db import models
from django.contrib.auth.models import User
from capstoneapi.models.job_posting import Job_Posting


class Applied(models.Model):
    posting = models.ForeignKey(Job_Posting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    isAccepted = models.BooleanField(default=False)
    isRejected = models.BooleanField(default=False)