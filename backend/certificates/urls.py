from django.urls import path
from certificates import views


urlpatterns = [
    path('', views.CertificateList.as_view())
]
    