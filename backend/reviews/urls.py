from django.urls import path
from reviews import views


urlpatterns = [
    path('', views.ReviewList.as_view())
]
