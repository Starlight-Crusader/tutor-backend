from django.db import models
from subjects.models import Subject
from profiles.models import Profile


class Course(models.Model):
    ONLINE = 1
    OFFLINE = 2
    LESSON_TYPE = (
        (ONLINE, "Online"),
        (OFFLINE, "Offline")
    )
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    price = models.PositiveIntegerField()
    lesson_format = models.IntegerField(choices=LESSON_TYPE)
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
