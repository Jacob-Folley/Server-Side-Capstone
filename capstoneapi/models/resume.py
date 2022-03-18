from django.db import models
from django.contrib.auth.models import User
from django import forms

class Resume(models.Model):
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=50)
    skills = models.ManyToManyField("Skills", through="Applicant_Skills", related_name='resume')