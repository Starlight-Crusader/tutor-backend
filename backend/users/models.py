from django.db import models

class TestUnit(models.Model):
    test_data = models.CharField(max_length=8)

class TestManyToMany(models.Model):
    test_record = models.ManyToManyField(TestUnit)

class Sertificate(models.Model):
    subject_name = models.CharField(max_length=32)
    document_path = models.CharField(max_length=64)

    is_verified = models.BooleanField(default=False)

class Subject(models.Model):
    subject_name = models.CharField(max_length=16)

class Rewiew(models.Model):
    author_fname = models.CharField(max_length=16)
    author_lname = models.CharField(max_length=16)
    
    rating = models.IntegerField()
    rewiew_text = models.CharField(max_length=256)

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

    profile_picture = models.CharField(max_length=64, blank=True)
    
    subjects = models.ManyToManyField(Subject, blank=True)
    sertificates = models.ManyToManyField(Sertificate, blank=True)
    rewiews = models.ManyToManyField(Rewiew, blank=True)