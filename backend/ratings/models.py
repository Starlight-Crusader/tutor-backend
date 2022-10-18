from django.db import models
from users.models import User


class Rating(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_value = models.PositiveSmallIntegerField()
    rating_time = models.DateTimeField(auto_now=True)
