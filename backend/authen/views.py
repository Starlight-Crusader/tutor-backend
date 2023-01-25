from django.contrib.auth import hashers
from rest_framework import generics, status, response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from authen import serializers
from users import models
from django.core.mail import send_mail
from backend import settings
import hashlib
import random
import datetime 
from profiles import models as profile_models
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


# AUTHENTICATION

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
        if user.check_password(serializer.data['password']) is False:
            error = {
                "message": "The auth. data is incorrect.",
                "status": 400
            }

            return response.Response(error)
    except models.User.DoesNotExist:
        error = {
            "message": "The auth. data is incorrect.",
            "status": 400
        }

        return response.Response(error)

    try:
        token = Token.objects.get(user=user)
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)

    user.last_login = datetime.datetime.now()
    data = {
        "id": user.id,
        "email": user.email,
        "is_staff": user.is_staff,
        "auth_token": token.key
    }

    return response.Response(data)


# PASSWORD RECOVERY

@api_view(['POST'])
@permission_classes([AllowAny])
def recovery_step_1(request):
    serializer = serializers.RecoveryStepOneSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
    except models.User.DoesNotExist:
        error = {
            "message": "The auth. data is incorrect.",
            "status": 400
        }

        return response.Response(error)

    recoveryCode = models.RecoveryCode.objects.filter(user_id=user.pk)

    if(recoveryCode):
        error = {
            "message": "You already have a token.",
            "status": 403
        }

        return response.Response(error)

    seed = str(random.randint(0, 1000))
    hashed = hashlib.md5(seed.encode())

    newCode = models.RecoveryCode.objects.create(
        recovery_code=str(hashed.hexdigest())[:5], 
        user=user,
        active_time=datetime.datetime.now()+datetime.timedelta(minutes=30)
    )
    
    newCode.save()
    
    send_mail(
        'Password recovery', 
        'This is an automated message. Your recovery code is: ' + newCode.recovery_code + '.', 
        'tutoringapp.testreciever@gmail.com',
        ['tutoringapp.testreciever@gmail.com'],
        fail_silently=False
    )

    message = {
        "message": "A recovery code was ceated and sent to your email.",
        "status": 200
    }

    return response.Response(message)


@api_view(['POST'])
@permission_classes([AllowAny])
def recovery_step_2(request):
    serializer = serializers.RecoveryStepTwoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        recoveryCode = models.RecoveryCode.objects.get(recovery_code=serializer.data['recovery_code'])
    except models.RecoveryCode.DoesNotExist:
        error = {
            "message": "This recovery code does not exist.",
            "status": 400
        }

        return response.Response(error)

    if(recoveryCode.is_active == False):
        error = {
            "message": "This recovery code is no longer valid.",
            "status": 400
        }

        return response.Response(error)
    
    if(serializer.data['new_password'] != serializer.data['confirm_new_password']):
        error = {
            "message": "Passwords do not coincide.",
            "status": 400
        }

        return response.Response(error)

    recoveryCode.user.password = hashers.make_password(serializer.data['new_password'])
    recoveryCode.user.save(update_fields=['password'])

    recoveryCode.is_active = False 
    recoveryCode.save(update_fields=['is_active'])

    message = {
        "message": "The password has been updated.",
        "status": 200
    }

    return response.Response(message)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = serializers.ChangePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(user = request.user.id)
    except models.User.DoesNotExist:
        error = {
            "message": "User does not exist.",
            "status": 400
        }

        return response.Response(error)

    if user.check_password(serializer.data['old_password']) is False:
        error = {
            "message": "Old password is incorrect.",
            "status": 400
        }

        return response.Response(error)

    if serializer.data['new_password'] != serializer.data['confirm_new_password']:
        error = {
            "message": "Passwords do not coincide.",
            "status": 400
        }

        return response.Response(error)

    user.password = hashers.make_password(serializer.data['new_password'])
    user.save(update_fields=['password'])

    message = {
        "message": "The password has been updated.",
        "status": 200
    }

    return response.Response(message)


# REGISTRATION

class RegisterUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    serializer_class = serializers.RegisterUserSerializer


class RegisterTutorView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    
    serializer_class = serializers.RegisterTutorSerializer


class RegisterStudentView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    
    serializer_class = serializers.RegisterStudentSerializer


# AUTH TOKENS HANDLING

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deactivate_expired(request):
    try:
        records = models.RecoveryCode.objects.all()
    except:
        message = {
            "message": "There are no recovery codes.",
            "status": 202
        }

        return response.Response(message)

    records = models.RecoveryCode.objects.filter(active_time__range=[datetime.now()-time.timedelta(days=360), datetime.now()]).update(is_active=False)

    message = {
        "message": "Expired codes were deactivated!",
        "status": 200
    }

    return response.Response(message)
