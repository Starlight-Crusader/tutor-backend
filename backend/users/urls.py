from django.urls import path
from users import views


urlpatterns = [
    path('', views.UserList.as_view()),
    path('recovery-codes', views.CodesList.as_view())
]
