from django.db import models
from users.models import User

class Rating(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating_value = models.IntegerField(min_value=1)
