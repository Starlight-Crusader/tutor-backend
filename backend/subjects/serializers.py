from pyexpat import model
from rest_framework import serializers
from subjects import models


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = '__all__'
