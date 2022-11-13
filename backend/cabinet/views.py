from rest_framework import generics, status, response, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from cabinet import serializers
from profiles import models


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_profile(request, pk=None):
    try:
        profile = models.Profile.objects.get(user=pk)
    except models.Profile.DoesNotExist:
        return response.Response('Profile does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CabinetSerializer(profile)
    serializer.is_valid(raise_exception=True)

    return response.Response(serializer.data)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def own_profile(request):
    try:
        profile = models.Profile.objects.get(user=request.user.id)
    except models.Profile.DoesNotExist:
        return response.Response('Profile does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CabinetSerializer(profile)
    serializer.is_valid(raise_exception=True)

    return response.Response(serializer.data)
