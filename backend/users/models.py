from django.db import models

# Create new apps for models

class Certificate(models.Model):
    # Foreign key to Sybjects?
    subject_name = models.CharField(max_length=32)
    document_path = models.FileField()

    is_verified = models.BooleanField(default=False)


class Subject(models.Model):
    subject_name = models.CharField(max_length=16)


class Rewiew(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rewiew_text = models.CharField(max_length=256)


class Rating(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating_value = models.IntegerField(min_value=1)

    # models.PositiveIntegerField()


class User(models.Model):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=32)

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)

    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    date_of_birth = models.DateField(null=True)
    location = models.CharField(max_length=32)

    profile_picture = models.FileField()
    
    subjects = models.ManyToManyField(Subject, blank=True)
    sertificates = models.ManyToManyField(Certificate, blank=True)
    rewiews = models.ManyToManyField(Rewiew, blank=True)


# Add profile model