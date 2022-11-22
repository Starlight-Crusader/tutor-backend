from rest_framework import generics
from ratings import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class RatingList(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
