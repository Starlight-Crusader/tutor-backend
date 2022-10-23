from rest_framework import generics
from certificates import models, serializers


class CertificateList(generics.ListCreateAPIView):
    queryset = models.Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
    