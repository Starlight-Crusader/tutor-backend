from pyexpat import model
from rest_framework import serializers
from profiles import models
from users import serializers as users_serializers
from django.db.models import Avg


class ProfileSerializer(serializers.ModelSerializer):
    user = users_serializers.UserSerializer(read_only=True)

    class Meta:
        model = models.Profile
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        avg_rating = instance.rating_recipients.aggregate(Avg("rating_value"))
        data["rating_value"] = avg_rating["rating_value__avg"]

        return data
