from rest_framework import generics
from subjects import models, serializers


class SubjectList(generics.ListCreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
