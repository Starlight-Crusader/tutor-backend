from rest_framework import generics, filters
from django.shortcuts import render
from courses import models
from courses import serializers
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    if Subscription.objects.get(student=models.Profile.objects.get(user_id=request.user.id).id, course=request.query_params.get('course')).exists():
        return response.Response('The user is already subscribed!',
                                status=status.HTTP_403_FORBIDDEN)
    else:
        Subscription.objects.create(student=models.Profile.objects.get(user_id=request.user.id).id, course=request.query_params.get('course'))

        return response.Response('Success!',
                                status=status.HTTP_200_OK)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_subsription(request):
    try:
        record = Subscription.objects.get(student=models.Profile.objects.get(user_id=request.user.id).id, course=request.query_params.get('course'))
    except models.Subscription.DoesNotExist:
        return response.Response('Error!',
                                status=status.HTTP_400_BAD_REQUEST)

    record.delete()

    return response.Response('Success!',
                            status=status.HTTP_200_OK)
