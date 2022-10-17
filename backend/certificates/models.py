from django.db import models

class Certificate(models.Model):
    subject_name = models.CharField(max_length=32)
    document_path = models.FileField()

    is_verified = models.BooleanField(default=False)