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


class RegisterStudentSerializer(serializers.ModelSerializer):
    user = users_serializers.UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = [
            'profile_type',
            'first_name',
            'last_name',
            'phone_number'
        ]
        
    def create(self, validated_data):
        validated_data['user_id'] = self.initial_data['user_id']
        validated_data['profile_type'] = self.initial_data['profile_type']
        validated_data['first_name'] = self.initial_data['first_name']
        validated_data['last_name'] = self.initial_data['last_name']
        validated_data['phone_number'] = self.initial_data['phone_number']
        profile = Profile.objects.create(**validated_data)
        
        return profile
   
    
class RegisterTutorSerializer(serializers.ModelSerializer):
    user = users_serializers.UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = [
            'profile_type',
            'first_name',
            'last_name',
            'phone_number',
            'contact_mail',
            'location'
        ]
        
    def create(self, validated_data):
        validated_data['user_id'] = self.initial_data['user_id']
        validated_data['profile_type'] = self.initial_data['profile_type']
        validated_data['first_name'] = self.initial_data['first_name']
        validated_data['last_name'] = self.initial_data['last_name']
        validated_data['phone_number'] = self.initial_data['phone_number']
        validated_data['contact_mail'] = self.initial_data['contact_mail']
        validated_data['location'] = self.initial_data['location']
        profile = Profile.objects.create(**validated_data)
        
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
