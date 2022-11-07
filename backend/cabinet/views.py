from rest_framework import generics, decorators, status, response
from django.contrib.auth.decorators import login_required
from cabinet import serializers
from profiles import models


@decorators.api_view(['GET'])
def get_profile(request, fk=None):
    try:
        profile = models.Profile.objects.get(user=fk)
    except models.Profile.DoesNotExist:
        return response.Response('Profile does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CabinetSerializer(profile)

    return response.Response(serializer.data)
