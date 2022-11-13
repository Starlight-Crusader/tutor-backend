from rest_framework import generics, filters
from django.shortcuts import render
from courses import models
from courses import serializers
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CourseList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['subject', 'lesson_format']
    