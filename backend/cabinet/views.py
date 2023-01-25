from rest_framework import status, response, permissions, authentication, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from cabinet import serializers
from profiles import models
from courses.models import Course
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# GET PROFILE DATA

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_profile(request, pk=None):
    try:
        profile = models.Profile.objects.get(user=pk)
    except models.Profile.DoesNotExist:
        error = {
            "message": "Profile was not found.",
            "status": 404
        }

        return response.Response(error)

    serializer = serializers.ProfileDataSerializer(profile)

    return response.Response(serializer.data)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def own_profile(request):
    try:
        profile = models.Profile.objects.get(user=request.user.id)
    except models.Profile.DoesNotExist:
        error = {
            "message": "Profile was not found.",
            "status": 404
        }

        return response.Response(error)

    serializer = serializers.ProfileDataSerializer(profile, context={'request': request})

    return response.Response(serializer.data)


# COURSES MANIPULATION

class NewCourseView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = serializers.NewCourseSerializer
    queryset = Course.objects.all()


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_course(request, pk=None):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        error = {
            "message": "Profile was not found.",
            "status": 404
        }

        return response.Response(error)

    if(course.user_id == request.user.id):
        course.delete()

        message = {
            "message": "The course has been deleted.",
            "status": 200
        }

        return response.Response(message)
    else:
        error = {
            "message": "You are not allowed to do that.",
            "status": 403
        }

        return response.Response(error)


class NewReviewView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = serializers.NewReviewSerializer


class NewRatingView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = serializers.NewRatingSerializer


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def modify_about_me(request):
    serializer = serializers.UpdateAboutMeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        profile = models.Profile.objects.get(user_id=request.user.id)
    except Profile.DoesNotExist:
        error = {
            "message": "Profile was not found.",
            "status": 404
        }

        return response.Response(error)

    profile.about_me = serializer.data['about_me']
    profile.save()

    message = {
        "message": "The about me has been updated.",
        "status": 200
    }

    return response.Response(message)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_subsription(request):
    try:
        record = Subscription.objects.get(student=models.Profile.objects.get(user_id=request.user.id).id, course=request.query_params.get('course'))
    except models.Subscription.DoesNotExist:
        error = {
            "message": "Record was not found.",
            "status": 404
        }

        return response.Response(error)

    record.delete()

    message = {
        "message": "The record was successfully deleted.",
        "status": 200
    }

    return response.Response(message)
