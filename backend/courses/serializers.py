from pyexpat import model
from rest_framework import serializers
from courses.models import Course
from users.models import User
from subjects.models import Subject


class CourseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    lesson_format = serializers.IntegerField()
    
    subject = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        course = Course.objects.create(
            user_id=User.objects.get(pk=validated_data['user_id']),
            lesson_format=validated_data['lesson_format'],
            subject=Subject.objects.get(pk=validated_data['subject']),
            price=validated_data['price']
        )
        return course
    #i have no fucking clue how to make the deletion serializer 
    # and not enough time to debug this one but it seems to not like the user_id field