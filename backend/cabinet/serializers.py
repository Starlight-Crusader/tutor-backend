from rest_framework import serializers
from profiles.models import Profile
#add a view to update profile and a view to get a profile specified by user_id

class CabinetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'
