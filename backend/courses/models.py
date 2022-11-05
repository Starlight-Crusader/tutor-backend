from django.db import models
from subjects.models import Subject
from profiles.models import Profile


class Course(models.Model):
    
    LESSON_TYPE = (
        (1, "ONLINE"),
        (2, "OFFLINE")
    )
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    lesson_format = models.IntegerField(choices=LESSON_TYPE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
