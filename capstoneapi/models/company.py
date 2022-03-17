from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    employer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)