from django.db import models
from users.models import User


class Review(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=1000)
    review_date = models.DateField(auto_now=True)
