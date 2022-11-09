from rest_framework import generics
from users import models, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_admin == False):
            return request.method in SAFE_METHODS
        else:
            return Response("You have no permissions for this operation!.")


class UserList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOnly]

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class CodesList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated|AdminOnly]

    queryset = models.RecoveryCode.objects.all()
    serializer_class = serializers.RecoveryCodeSerializer
