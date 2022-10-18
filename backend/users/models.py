from django.db import models
from django.contrib.auth.models import AbstractBaseUser 


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    reg_date = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    