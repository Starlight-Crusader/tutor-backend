from django.db import models
from users.models import User

class Review(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rewiew_text = models.CharField(max_length=256)