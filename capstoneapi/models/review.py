from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    postingId = models.ForeignKey("Job_Posting", on_delete=models.CASCADE)
    applicantId = models.ForeignKey("Applied", on_delete=models.CASCADE)
    employerId = models.ForeignKey(
        User, on_delete=models.CASCADE)
    isAccepted = models.BooleanField(default=False)
    isRejected = models.BooleanField(default=False)