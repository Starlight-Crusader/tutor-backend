from django.urls import path
from cabinet import views


urlpatterns = [
    path('<int:fk>', views.get_profile)
]
