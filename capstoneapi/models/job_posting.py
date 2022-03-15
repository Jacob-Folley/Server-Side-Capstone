from django.db import models
from django.contrib.auth.models import User


class Job_Posting(models.Model):
    employer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    skills = models.ManyToManyField("Skills", through="Posting_Skill", related_name='postings')