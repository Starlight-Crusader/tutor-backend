from datetime import datetime
from django.contrib.auth import hashers
from rest_framework import generics, decorators, status, response
from authen import serializers
from users import models


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
    

class PasswordRecoveryView():
    #TODO: request password by email; create code based on the model in users
    #TODO: replace old password; input new password (look in changepassword)
    pass

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
