from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    is_verified = models.BooleanField(default=False)

    date_of_birth = models.DateField(null=True)
    location = models.CharField(max_length=32)

    profile_picture = models.FileField()
    
    subjects = models.ManyToManyField(Subject, blank=True)
    sertificates = models.ManyToManyField(Certificate, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
