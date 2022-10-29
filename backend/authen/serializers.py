from rest_framework import serializers
from users import models
from django.contrib.auth import hashers


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Parola nu coincide.')
        return attrs

    def create(self, validated_data):
        password = hashers.make_password(validated_data['password'])
        user = models.User.objects.create(
            email=validated_data['email'],
            password=password
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RecoveryStepOneSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()


class RecoveryPasswordSerializer(serializers.Serializer):
    pass
#TODO: RecoveryCode serializer, views, url; 