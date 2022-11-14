from django.db import models
from users.models import User
from profiles.models import Profile


class Review(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    for_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=1000)
    review_date = models.DateField(auto_now=True)
