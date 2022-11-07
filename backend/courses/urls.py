from django.urls import path
from courses import views


urlpatterns = [
    path('', views.CreateCourseView.as_view()),
    path('<int:pk>', views.DetailedCourseView.as_view())
]
    