from datetime import datetime
from django.contrib.auth import hashers
from rest_framework import generics, decorators, status, response
from authen import serializers
from users import models
from django.core.mail import send_mail
from backend import settings
import hashlib
import random
import datetime as time
from profiles import models as profile_models


@decorators.api_view(['POST'])
def login_view(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
        if user.check_password(serializer.data['password']) is False:
            return response.Response('Password is incorrect.',
                                     status=status.HTTP_400_BAD_REQUEST)
    except models.User.DoesNotExist:
        return response.Response('User does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    user.last_login = datetime.datetime.now()
    data = {
        "id": user.id,
        "email": user.email,
        "is_admin": user.is_admin,
    }

    return response.Response(data)
    

@decorators.api_view(['POST'])
def recovery_step_1(request):
    serializer = serializers.RecoveryStepOneSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
    except models.User.DoesNotExist:
        return response.Response('User does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    recoveryCode = models.RecoveryCode.objects.filter(user_id=user.pk)

    if(recoveryCode):
        return response.Response('You already have a token.',
                                 status=status.HTTP_400_BAD_REQUEST)

    seed = str(random.randint(0, 1000))
    hashed = hashlib.md5(seed.encode())

    newCode = models.RecoveryCode.objects.create(recovery_code=str(hashed.hexdigest())[:5], 
                                                 user=user,
                                                 active_time=datetime.datetime.now()+datetime.timedelta(minutes=30))
    
    newCode.save()
    
    send_mail('Password recovery', 
              'This is an automated message. Your recovery code is: ' + newCode.recovery_code + '.', 
              'tutoringapp.testreciever@gmail.com',
              ['tutoringapp.testreciever@gmail.com'],
              fail_silently=False)

    return response.Response('A recovery code was ceated and send to your email.')


@decorators.api_view(['POST'])
def recovery_step_2(request):
    serializer = serializers.RecoveryStepTwoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        recoveryCode = models.RecoveryCode.objects.get(recovery_code=serializer.data['recovery_code'])
    except models.RecoveryCode.DoesNotExist:
        return response.Response('This recovery code does not exist.',
                                 status=status.HTTP_400_BAD_REQUEST)

    if(recoveryCode.is_active == False):
        return response.Response('This recovery code is no longer valid.',
                                 status=status.HTTP_400_BAD_REQUEST)
    
    if(serializer.data['new_password'] != serializer.data['confirm_new_password']):
        return response.Response('Passwords do not coincide!',
                                 status=status.HTTP_400_BAD_REQUEST)

    recoveryCode.user.password = hashers.make_password(serializer.data['new_password'])
    recoveryCode.user.save(update_fields=['password'])

    recoveryCode.is_active = False 
    recoveryCode.save(update_fields=['is_active'])

    return response.Response('The password has been updated.')


class RegisterUserView(generics.CreateAPIView):
    serializer_class = serializers.RegisterUserSerializer


class RegisterTutorView(generics.ListCreateAPIView):
    queryset = profile_models.Profile.objects.all()
    serializer_class = serializers.RegisterTutorSerializer


class RegisterStudentView(generics.ListCreateAPIView):
    queryset = profile_models.Profile.objects.all()
    serializer_class = serializers.RegisterStudentSerializer


class LogoutView():
    #TODO: delete token after sign-out
    pass


@decorators.api_view(['POST'])
def change_password(request, pk=None):
    serializer = serializers.ChangePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(id=pk)
    except models.User.DoesNotExist:
        return response.Response('User does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    if user.check_password(serializer.data['old_password']) is False:
        return response.Response('Old password is incorrect.',
                                 status=status.HTTP_400_BAD_REQUEST)

    if serializer.data['new_password'] != serializer.data['confirm_new_password']:
        return response.Response('Passwords do not coincide.',
                                 status=status.HTTP_400_BAD_REQUEST)

    user.password = hashers.make_password(serializer.data['new_password'])
    user.save(update_fields=['password'])

    return response.Response('The password has been updated.')


@decorators.api_view(['PATCH'])
def deactivate_expired(request):
    try:
        records = models.RecoveryCode.objects.all()
    except:
        return response.Response('There are no recovery codes.',
                                 status=status.HTTP_202_ACCEPTED)

    records = models.RecoveryCode.objects.filter(active_time__range=[datetime.now()-time.timedelta(days=360), datetime.now()]).update(is_active=False)

    return response.Response('Expired codes were deactivated!')
