from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from profiles import models, serializers


class ProfileList(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    
