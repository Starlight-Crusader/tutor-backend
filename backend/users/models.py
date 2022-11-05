from enum import _auto_null
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser 


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    reg_date = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'


class RecoveryCode(models.Model):
    recovery_code = models.CharField(max_length=5)
    created_time = models.DateTimeField(auto_now=True)
    active_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    