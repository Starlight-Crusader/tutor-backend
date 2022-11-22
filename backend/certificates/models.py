from django.db import models
from profiles.models import Profile


class Certificate(models.Model):
    document_path = models.FileField(upload_to="docs/certificates")
    is_verified = models.BooleanField(default=False)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
