from rest_framework import generics
from reviews import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class ReviewList(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
