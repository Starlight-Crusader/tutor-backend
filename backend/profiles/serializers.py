from pyexpat import model
from rest_framework import serializers
from profiles import models


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = '__all__'
        