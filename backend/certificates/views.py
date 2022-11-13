from rest_framework import generics
from certificates import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CertificateList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
    