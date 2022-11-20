from pyexpat import model
from rest_framework import serializers
from courses.models import Course
from users.models import User
from subjects.serializers import SubjectSerializer
from users.serializers import UserSerializer
from subjects.models import Subject

class CourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'
