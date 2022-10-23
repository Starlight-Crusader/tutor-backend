from pyexpat import model
from rest_framework import serializers
from certificates import models


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Certificate
        fields = '__all__'
        