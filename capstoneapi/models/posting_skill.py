from django.db import models
from django.contrib.auth.models import User


class Posting_Skill(models.Model):
    skill = models.ForeignKey("Skills", on_delete=models.CASCADE)
    posting = models.ForeignKey("Job_Posting", on_delete=models.CASCADE)