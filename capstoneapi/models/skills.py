from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    skill = models.CharField(max_length=25)