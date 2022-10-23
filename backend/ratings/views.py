from rest_framework import generics
from ratings import models, serializers


class RatingList(generics.ListCreateAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
