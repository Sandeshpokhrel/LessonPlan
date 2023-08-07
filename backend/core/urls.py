from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import  UserRegistrationView, UserLoginView, UserProfileView, SubjectListCreateAPI, SectionYearCreateAPI, ChapterTopicAPI, TopicCreateAPI, AssignmentCreateAPI, ResourceCreateAPI, SubjectDeleteAPI, PlanListCreateAPI, PlanChapterCreateAPI, ChapterDeleteAPI



urlpatterns = [
    path('auth/users/', UserRegistrationView.as_view()),
    path('auth/jwt/create/', UserLoginView.as_view()),
    path('auth/jwt/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('auth/users/me/', UserProfileView.as_view()),
    path('subjects/', SubjectListCreateAPI.as_view()),
    path('subjects/<int:pk>/', SubjectDeleteAPI.as_view()),
    path('chapter/<int:pk>/', ChapterDeleteAPI.as_view()),
    path('sections/', SectionYearCreateAPI.as_view()),
    path('sections/<int:id>/chapters/', ChapterTopicAPI.as_view()),
    path('topics/', TopicCreateAPI.as_view()),
    path('assignments/', AssignmentCreateAPI.as_view()),
    path('resources/', ResourceCreateAPI.as_view()),
    path('sections/<int:id>/plan/', PlanListCreateAPI.as_view()),
    path('plan/chapter/', PlanChapterCreateAPI.as_view()),
]
