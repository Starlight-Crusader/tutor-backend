from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=32)

    is_admin = models.BooleanField(default=False)
