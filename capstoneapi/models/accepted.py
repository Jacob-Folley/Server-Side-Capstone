from django.db import models
from django.contrib.auth.models import User
from capstoneapi.models.job_posting import Job_Posting


class Accepted(models.Model):
    posting = models.ForeignKey(Job_Posting, on_delete=models.CASCADE, related_name ='applied')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)