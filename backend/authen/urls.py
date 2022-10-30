from django.urls import path
from authen import views


urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.login_view),
    path('change-password/<int:pk>', views.change_password),
    path('recovery/step-1', views.recovery_step_1),
    path('recovery/step-2', views.recovery_step_2)
]
