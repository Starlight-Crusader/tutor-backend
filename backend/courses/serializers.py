from pyexpat import model
from rest_framework import serializers
from courses import models
from subjects.serializers import SubjectSerializer
from profiles.serializers import ProfileSerializer


class CourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = models.Course
        fields = '__all__'
        