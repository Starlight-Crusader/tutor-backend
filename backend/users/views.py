from rest_framework import generics
from users import models, serializers


class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class CodesList(generics.ListCreateAPIView):
    queryset = models.RecoveryCode.objects.all()
    serializer_class = serializers.RecoveryCodeSerializer