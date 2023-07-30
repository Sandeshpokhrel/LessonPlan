from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .renderers import UserRenderer
from .models import Subject, SectionYear, Chapter, Topic
from .serializers import UserRegisterationSerializer, UserLoginSerializer, UserProfileSerializer, SubjectViewSerializer, SubjectCreateSerializer, SectionCreateSerializer, ChapterViewSerializer, ChapterCreateSerializer, TopicCreateSerializer


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegisterationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    password = serializer.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SubjectListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get_queryset(self):
        return Subject.objects.prefetch_related('sectionyear_set').all().filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubjectCreateSerializer
        elif self.request.method == 'GET':
            return SubjectViewSerializer



class SectionYearCreateAPI(CreateAPIView):
    queryset = SectionYear.objects.all()
    serializer_class = SectionCreateSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]


class ChapterTopicAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get_queryset(self):
        return Chapter.objects.prefetch_related('topic_set').all().filter(section_year=self.kwargs['id'])
   
    def get_serializer_class(self):
        if self.request.method == 'GET':
          return ChapterViewSerializer
        elif self.request.method == 'POST':
          return ChapterCreateSerializer


class TopicCreateAPI(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
