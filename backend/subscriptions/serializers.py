from pyexpat import model
from rest_framework import serializers
from subscriptions import models


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subscription
        fields = '__all__'
        