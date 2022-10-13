from django.db import models

class Test(models.Model):
    test_data = models.CharField(max_length=8)

"""
class Sertificate(models.Model):
    subject = models.CharField(max_length=32)
    document = models.CharField(max_length=64)

    is_verified = models.BooleanField()
"""

class User(models.Model):
    emal = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    is_student = models.BooleanField()
    is_pupil = models.BooleanField()
    is_admin = models.BooleanField()
    is_verified = models.BooleanField()

    date_of_birth = models.DateField(blank=True)
    location = models.CharField(max_length=32, blank=True)

    # profile_picture = models.CharField(max_length=64, blank=True)

    """
    subjects = ArrayField(
        models.CharField(max_length=16, blank=True),
        size=8
    )

    sertificates = ArrayField(
        models.Sertificate(blank=True),
        size=8
    )
    """