from rest_framework import generics, filters
from django.shortcuts import render
from courses import models
from courses import serializers
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import FilterSet, RangeFilter


class DisplayCourses(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    filter_backends = (filters.DjangoFilterBackend,)

    filterset_fields = ['subject', 'lesson_format', 'location']

    def get_queryset(self):
        min_value = int(self.request.query_params.get('min'))
        max_value = int(self.request.query_params.get('max'))

        filtered_courses = models.Course.objects.filter(price__range=(min_value, max_value))

        return filtered_courses
        