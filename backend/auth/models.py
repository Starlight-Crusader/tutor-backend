from django.db import models

# class Sertificate(models.Model): ...

class User(models.Model):
    emal = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    is_student = models.BooleanField()
    is_pupil = models.BooleanField()
    is_admin = model.BooleanField()

    date_of_birth = model.DateField()
    location = model.CharField(max_length=32)

    profile_picture = model.CharField(max_length=64)
    