from datetime import datetime
from django.contrib.auth import hashers
from rest_framework import generics, decorators, status, response
from authen import serializers
from users import models
from django.core.mail import send_mail
from backend import settings
import hashlib
import random
import datetime


@decorators.api_view(['POST'])
def login_view(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
        if user.check_password(serializer.data['password']) is False:
            return response.Response('Parola incorecta.',
                                     status=status.HTTP_400_BAD_REQUEST)
    except models.User.DoesNotExist:
        return response.Response('Utilizatorul nu exista.',
                                 status=status.HTTP_404_NOT_FOUND)

    user.last_login = datetime.now()
    data = {
        "id": user.id,
        "email": user.email,
        "is_admin": user.is_admin,
    }

    return response.Response(data)
    

@decorators.api_view(['POST'])
def recovery_step_1(request, pk=None):
    serializer = serializers.RecoveryStepOneSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.User.objects.get(email=serializer.data['email'])
    except models.User.DoesNotExist:
        return response.Response('Utilizatorul nu exista.',
                                 status=status.HTTP_404_NOT_FOUND)

    recoveryCode = models.RecoveryCode.objects.all()
    recoveryCode = models.RecoveryCode.objects.filter(user=user)

    if(recoveryCode):
        return response.Response('You already have a token.',
                                 status=status.HTTP_400_BAD_REQUEST)

    seed = str(random.randint(0, 1000))
    hashed = hashlib.md5(seed.encode())

    newCode = models.RecoveryCode.objects.create(recovery_code=str(hashed.hexdigest())[:5], 
                                                 user=user,
                                                 active_time=datetime.datetime.now()+datetime.timedelta(minutes=1))
    
    newCode.save()
    
    send_mail('Password recovery', 
              'This is an automated message. Your recovery code is: ' + newCode.recovery_code + '.', 
              'tutoringapp.testreciever@gmail.com',
              ['tutoringapp.testreciever@gmail.com'],
              fail_silently=False)

    return response.Response('A recovery code was ceated and send to your email.')

@decorators.api_view(['POST'])
def recovery_step_2(request, pk=None):
    serializer = serializers.RecoveryStepTwoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = models.RecoveryCode.objects.get(recovery_code=serializer.data['recovery_code']).user
    except models.User.DoesNotExist:
        return response.Response('This recovery code is not valid!',
                                 status=status.HTTP_404_NOT_FOUND)
    
    if(serializer.data['new_password'] != serializer.data['confirm_new_password']):
        return response.Response('Pass-s do not coincide!',
                                 status=status.HTTP_400_BAD_REQUEST)

    password = hashers.make_password(serializer.data['new_password'])
    user.password = password
    user.save()

    code_record = models.RecoveryCode.objects.get(recovery_code=serializer.data['recovery_code'])
    code_record.delete()
    code_record.save()

    return response.Response('Parola a fost modificata.')

class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer

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
        return response.Response('Utilizatorul nu exista.',
                                 status=status.HTTP_404_NOT_FOUND)

    if user.check_password(serializer.data['old_password']) is False:
        return response.Response('Parola veche incorecta.',
                                 status=status.HTTP_400_BAD_REQUEST)

    if serializer.data['new_password'] != serializer.data['confirm_new_password']:
        return response.Response('Parola noua nu coincide.',
                                 status=status.HTTP_400_BAD_REQUEST)

    password = hashers.make_password(serializer.data['new_password'])
    user.password = password
    user.save()

    return response.Response('Parola a fost modificata.')
