from django.db import models
from django.contrib.auth.models import User


class Job_Posting(models.Model):
    employer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=10000)
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name='User', null=True)
    skills = models.ManyToManyField("Skills", through="Posting_Skill", related_name='postings')
  