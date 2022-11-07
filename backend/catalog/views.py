from rest_framework import generics, filters
from django.shortcuts import render
from courses.models import Course
from courses import serializers
import django_filters


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

    filterset_fields = ['subject', 'lesson_format']
    