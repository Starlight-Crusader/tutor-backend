from rest_framework import generics, decorators, status, response
from django.contrib.auth.decorators import login_required
from cabinet import serializers
from profiles import models


@decorators.api_view(['GET'])
def get_profile(request, pk=None):
    try:
        profile = models.Profile.objects.get(user=pk)
    except models.Profile.DoesNotExist:
        return response.Response('Profile does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CabinetSerializer(profile)
    serializer.is_valid(raise_exception=True)

    return response.Response(serializer.data)

#TODO: def own_profile()
