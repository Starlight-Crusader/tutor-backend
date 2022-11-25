from django.urls import path
from cabinet import views


urlpatterns = [
    path('<int:pk>', views.get_profile),
    path('me', views.own_profile),
    path('me/add-new-course', views.NewCourseView.as_view()),
    path('me/delete-course/<int:pk>', views.remove_course),
    path('me/update-about-me', views.modify_about_me),
    path('<int:pk>/new-review', views.NewReviewView.as_view()),
    path('<int:pk>/new-rating', views.NewRatingView.as_view())
]
