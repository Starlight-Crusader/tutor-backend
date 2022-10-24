from django.db import models


class Certificate(models.Model):
    document_path = models.FileField(upload_to="docs/certificates")
    is_verified = models.BooleanField(default=False)
