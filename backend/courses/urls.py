from django.urls import path
from courses import views


urlpatterns = [
    path('', views.CourseList.as_view()),
    path('add-course', views.CreateCourseView.as_view()),
    path('remove-course/<int:pk>', views.remove_course)
]
    