from pyexpat import model
from rest_framework import serializers
from courses.models import Course
from users.models import User
from users import serializers as users_serializers
from subjects import serializers as subjects_serializers
from subjects.models import Subject


class CourseCreationSerializer(serializers.ModelSerializer):
    subject = subjects_serializers.SubjectSerializer(read_only=True)
    user = users_serializers.UserSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = [
            'price',
            'lesson_format',
            'subject',
            'user'
        ]

    def create(self, validated_data):
        validated_data['subject_id'] = self.initial_data['subject_id']
        validated_data['user_id'] = self.initial_data['user_id']
        validated_data['price'] = self.initial_data['price']
        validated_data['lesson_format'] = self.initial_data['lesson_format']

        course = Course.objects.create(**validated_data)
    
        return course
