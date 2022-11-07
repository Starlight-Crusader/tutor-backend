from rest_framework import generics, filters
from django.shortcuts import render
from courses import models
from courses import serializers
from django_filters import rest_framework as filters


class CourseList(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['subject', 'lesson_format']
    