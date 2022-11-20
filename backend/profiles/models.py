from importlib.resources import path
from random import choices
from django.db import models
from users.models import User
from phone_field import PhoneField


class Profile(models.Model):
    TUTOR = 1
    STUDENT = 2
    PROFILE_TYPE = (
        (TUTOR, "Tutor"),
        (STUDENT, "Student")
    )

    profile_type = models.IntegerField(choices=PROFILE_TYPE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_mail = models.EmailField(null=True, unique=True)

    phone_number = PhoneField(null=True)
    about_me = models.TextField(null=True, max_length=1000)

    is_verified = models.BooleanField(default=False)
    is_trusted = models.BooleanField(default=False)

    date_of_birth = models.DateField(null=True)
    location = models.CharField(max_length=50)
    
    profile_picture = models.FileField(upload_to="docs/pfp", blank=True)
