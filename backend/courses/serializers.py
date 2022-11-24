from pyexpat import model
from rest_framework import serializers
from courses.models import Course
from profiles.models import Profile
from subjects.serializers import SubjectSerializer
from profiles.serializers import ProfileSerializer
from subjects.models import Subject

class CourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'
        