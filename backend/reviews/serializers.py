from pyexpat import model
from rest_framework import serializers
from reviews import models

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'
        