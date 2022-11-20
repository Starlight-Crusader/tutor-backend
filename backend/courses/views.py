from rest_framework import generics
from courses import models, serializers
from rest_framework import generics,  status, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class CourseList(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
