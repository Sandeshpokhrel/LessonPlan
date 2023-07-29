from django.urls import path

from .views import  UserRegistrationView, UserLoginView, UserProfileView, SubjectListCreateAPI, SectionYearCreateAPI


urlpatterns = [
    path('auth/users/', UserRegistrationView.as_view()),
    path('auth/jwt/create/', UserLoginView.as_view()),
    path('auth/users/me/', UserProfileView.as_view()),
    path('subjects/', SubjectListCreateAPI.as_view()),
    path('sections/', SectionYearCreateAPI.as_view()),
]
