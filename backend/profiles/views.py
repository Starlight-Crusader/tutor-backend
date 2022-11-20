from rest_framework import generics
from profiles import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
