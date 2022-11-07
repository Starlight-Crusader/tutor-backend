from django.urls import path
from cabinet import views


urlpatterns = [
    path('<int:pk>', views.get_profile)
]
