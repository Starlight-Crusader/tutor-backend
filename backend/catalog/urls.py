from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.DisplayCourses.as_view())
]