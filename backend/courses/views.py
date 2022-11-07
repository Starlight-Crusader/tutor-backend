from rest_framework import generics
from courses import models, serializers
from rest_framework import generics, decorators, status, response


class CreateCourseView(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer


@decorators.api_view(['DELETE'])
def remove_course(request, pk=None):
    try:
        course = models.Course.objects.get(id=pk)
    except models.Course.DoesNotExist:
        return response.Response('Cource does not exist.',
                                 status=status.HTTP_404_NOT_FOUND)

    course.delete()

    return response.Response('The course has been deleted.')


class DetailedCourseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseCreationSerializer
