from pyexpat import model
from rest_framework import serializers
from courses import models


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.Course
        fields = '__all__'
        