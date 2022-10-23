from django.urls import path
from subjects import views


urlpatterns = [
    path('', views.SubjectList.as_view())
]
