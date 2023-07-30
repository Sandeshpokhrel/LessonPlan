from django.urls import path

from .views import  UserRegistrationView, UserLoginView, UserProfileView, SubjectListCreateAPI, SectionYearCreateAPI, ChapterTopicAPI, TopicCreateAPI, AssignmentCreateAPI


urlpatterns = [
    path('auth/users/', UserRegistrationView.as_view()),
    path('auth/jwt/create/', UserLoginView.as_view()),
    path('auth/users/me/', UserProfileView.as_view()),
    path('subjects/', SubjectListCreateAPI.as_view()),
    path('sections/', SectionYearCreateAPI.as_view()),
    path('sections/<int:id>/chapters/', ChapterTopicAPI.as_view()),
    path('topics/', TopicCreateAPI.as_view()),
    path('assignments/', AssignmentCreateAPI.as_view()),
]
