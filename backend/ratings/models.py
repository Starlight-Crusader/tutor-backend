from django.db import models
from profiles.models import Profile


class Rating(models.Model):
    rating_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rating_authors')
    rating_for = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rating_recipients')

    rating_value = models.PositiveSmallIntegerField()
    rating_time = models.DateTimeField(auto_now=True)
