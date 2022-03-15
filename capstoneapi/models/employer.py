from django.db import models
from django.contrib.auth.models import User


class Employer(models.Model):
    company = models.CharField(max_length=25)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

