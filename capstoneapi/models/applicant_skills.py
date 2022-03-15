from django.db import models
from django.contrib.auth.models import User


class Applicant_Skills(models.Model):
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE)
    skills = models.ForeignKey("Skills", on_delete=models.CASCADE)