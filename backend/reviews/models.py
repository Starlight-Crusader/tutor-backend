from django.db import models
from profiles.models import Profile


class Review(models.Model):
    review_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='review_authors')
    review_for = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='review_recipients')

    review_text = models.TextField(max_length=1000)
    review_date = models.DateField(auto_now=True)
