from django.db import models
#from subjects import models
#try making subjects a foreign key

class Certificate(models.Model):
    subject_name = models.CharField(max_length=100)
    document_path = models.FileField(upload_to="docs/certificates")
    is_verified = models.BooleanField(default=False)
