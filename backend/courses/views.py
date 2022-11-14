from rest_framework import generics
from courses import models, serializers
from rest_framework import generics,  status, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class CreateCourseView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_course(request, pk=None):
    try:
        course = models.Course.objects.get(id=pk)
    except models.Course.DoesNotExist:
        return response.Response('Course does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    if(course.user_id == request.user.id):
        course.delete()
        return response.Response('The course has been deleted.')
    else:
        return response.Response('You are not allowed to do that!')


class DetailedCourseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer
