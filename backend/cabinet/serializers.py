from rest_framework import serializers
from profiles.models import Profile

class CabinetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        exclude = ['id', 'user']
