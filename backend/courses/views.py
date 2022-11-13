from rest_framework import generics
from courses import models, serializers
from rest_framework import generics,  status, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class CreateCourseView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_course(request, pk=None):
    try:
        course = models.Course.objects.get(id=pk)
    except models.Course.DoesNotExist:
        return response.Response('Cource does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    course.delete()

    return response.Response('The course has been deleted.')


class DetailedCourseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer
