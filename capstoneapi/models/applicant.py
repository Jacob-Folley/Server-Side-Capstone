from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    isEmployer = models.BooleanField()

