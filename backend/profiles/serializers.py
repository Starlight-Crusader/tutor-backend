from pyexpat import model
from rest_framework import serializers
from profiles import models
from users import serializers as users_serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = users_serializers.UserSerializer(read_only=True)

    class Meta:
        model = models.Profile
        fields = '__all__'

    #TODO: def to_representation(self, instance):
