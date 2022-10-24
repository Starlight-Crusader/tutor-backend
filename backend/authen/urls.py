from django.urls import path
from authen import views


urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.login_view),
    path('change-password/<int:pk>', views.change_password)
]
