from rest_framework import generics, decorators, status, response
from django.contrib.auth.decorators import login_required
from users import models
from cabinet import serializers
from profiles import models
#add a view to update profile and a view to get a profile specified by user_id

@decorators.api_view(['GET'])
def cabinet_view(request):
    serializer = serializers.CabinetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        profile = models.Profile.objects.get(user_id=serializer.data['user_id'])
    except models.Profile.DoesNotExist:
        return response.Response('Profile was not created.',
                                 status=status.HTTP_404_NOT_FOUND)

    return profile
#i hope this is correct but it most likely isn't :')
