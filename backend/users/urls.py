from django.urls import path
from users import views


urlpatterns = [
    path('users-list', views.UserList.as_view()),
    path('recovery-codes-list', views.CodesList.as_view())
]
