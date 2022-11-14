from django.db import models
from users.models import User
from profiles.models import Profile


class Rating(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    for_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating_value = models.PositiveSmallIntegerField()
    rating_time = models.DateTimeField(auto_now=True)
