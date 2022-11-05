from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.CourseList.as_view())
]