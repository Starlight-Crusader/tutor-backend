from rest_framework import serializers
from profiles.models import Profile
from django.db.models import Avg

class CabinetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        exclude = ['id', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        avg_rating = instance.rating_set.aggregate(Avg("rating_value"))
        data["rating_value"] = avg_rating["rating_value__avg"]

        reviews = instance.rating_set.all().values()
        data["reviews"] = reviews

        return data
