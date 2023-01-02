from django.db import models
from profiles.models import Profile
from courses.models import Course


class Subscription(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
