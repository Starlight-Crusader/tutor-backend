from rest_framework import serializers
from users import models
from profiles.models import Profile
from django.contrib.auth import hashers
from phonenumber_field.phonenumber import PhoneNumber
from users import serializers as users_serializers


class RegisterUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('The passwords do not coincide.')
        return attrs

    def create(self, validated_data):
        password = hashers.make_password(validated_data['password'])
        user = models.User.objects.create(
            email=validated_data['email'],
            password=password
        )
        return user


class RegisterTutorSerializer(serializers.Serializer):
    profile_type = serializers.IntegerField()
    
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    phone_number = serializers.CharField()
    contact_mail = serializers.EmailField()

    location = serializers.CharField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        profile = Profile.objects.create(
            profile_type=validated_data['profile_type'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=PhoneNumber.from_string(validated_data['phone_number']),
            contact_mail=validated_data['contact_mail'],
            location=validated_data['location'],
            user=models.User.objects.get(pk=validated_data['user_id'])
        )
        return profile


class RegisterStudentSerializer(serializers.Serializer):
    profile_type = serializers.IntegerField()
    
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    phone_number = serializers.CharField()

    user_id = serializers.IntegerField()

    def create(self, validated_data):
        profile = Profile.objects.create(
            profile_type=validated_data['profile_type'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=PhoneNumber.from_string(validated_data['phone_number']),
            user=models.User.objects.get(pk=validated_data['user_id'])
        )
        return profile


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RecoveryStepOneSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecoveryStepTwoSerializer(serializers.Serializer):
    recovery_code = serializers.CharField()

    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()
