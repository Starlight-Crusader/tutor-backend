from rest_framework import generics
from subjects import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class SubjectList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
