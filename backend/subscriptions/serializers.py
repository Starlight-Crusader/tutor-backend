from pyexpat import model
from rest_framework import serializers
from subscriptions import models
from profiles.serializers import ProfileSerializer
from courses.serializers import CourseSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    student = ProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = models.Subscription
        fields = '__all__'
