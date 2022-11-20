from django.urls import path
from authen import views


urlpatterns = [
    path('register/register-user', views.RegisterUserView.as_view()),
    path('register/register-tutor', views.RegisterTutorView.as_view()),
    path('register/register-student', views.RegisterStudentView.as_view()),
    path('login', views.login_view),
    path('change-password', views.change_password),
    path('recovery/step-1', views.recovery_step_1),
    path('recovery/step-2', views.recovery_step_2),
    path('rcodes-deactivate', views.deactivate_expired)
]
