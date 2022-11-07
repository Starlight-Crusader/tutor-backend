from django.db import models
from subjects.models import Subject
from users.models import User


class Course(models.Model):
    
    LESSON_TYPE = (
        (1, "ONLINE"),
        (2, "OFFLINE")
    )
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    lesson_format = models.IntegerField(choices=LESSON_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
