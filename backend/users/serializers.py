from pyexpat import model
from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        # exclude = ['password']
        fields = '__all__'
        
class RecoveryCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RecoveryCode
        fields= '__all__'
