from django.db import models
from django.contrib.auth.models import User
from django import forms

class Resume(models.Model):
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to='resumeimages', height_field=None, width_field=None, max_length=None, null=True)
    skills = models.ManyToManyField("Skills", through="Applicant_Skills", related_name='resume')