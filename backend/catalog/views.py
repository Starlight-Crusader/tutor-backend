from rest_framework import generics, filters, response, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render
from courses import models
from courses import serializers
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import FilterSet, RangeFilter
from subscriptions.models import Subscription
from users.models import User


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


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_subsription(request):
    if models.Profile.objects.get(user_id=request.user.id).profile_type != 2:
        return response.Response(
            'You are not allowed to perform this action!',
            status=status.HTTP_403_BAD_REQUEST
        )

    try:
        record = Subscription.objects.get(student=models.Profile.objects.get(user_id=request.user.id), course_id=request.query_params.get('course'))
    except Subscription.DoesNotExist:
        Subscription.objects.create(student=models.Profile.objects.get(user_id=request.user.id), course_id=request.query_params.get('course'))

        return response.Response(
            'The subscription was successfully created.',
            status=status.HTTP_200_OK
        )

    return response.Response(
        'Something went wrong!',
        status=status.HTTP_403_FORBIDDEN
    )
