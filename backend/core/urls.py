from django.urls import path

from .views import SubjectListCreateAPI, SectionYearCreateAPI


urlpatterns = [
    path('subjects/', SubjectListCreateAPI.as_view()),
    path('sections/', SectionYearCreateAPI.as_view()),
]
