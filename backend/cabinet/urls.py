from django.urls import path
from cabinet import views


urlpatterns = [
    path('<int:pk>', views.get_profile),
    path('me', views.own_profile),
    path('add-new-course', views.NewCourseView.as_view()),
    path('delete-course/<int:pk>', views.remove_course),
    path('<int:pk>/new-review', views.NewReviewView.as_view()),
    path('<int:pk>/new-rating', views.NewRatingView.as_view())
]
