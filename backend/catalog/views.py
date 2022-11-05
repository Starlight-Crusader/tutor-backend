from rest_framework import generics, filters
from django.shortcuts import render
from courses.models import Course
from courses.serializers import CourseSerializer
import django_filters


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filterset_fields = ['subject', 'lesson_format']
        