from django.urls import path
from rcodes_handling import views


urlpatterns = [
    path('delete-expired', views.delete_expired)
]
