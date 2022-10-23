from pyexpat import model
from rest_framework import serializers
from ratings import models


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rating
        fields = '__all__'
      