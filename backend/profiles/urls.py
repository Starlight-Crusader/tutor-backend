from django.urls import path
from profiles import views


urlpatterns = [
    path('', views.ProfileList.as_view())
]
