from rest_framework.generics import ListCreateAPIView, CreateAPIView 
from rest_framework.permissions import IsAuthenticated

from .models import Subject, SectionYear
from .serializers import SubjectViewSerializer, SubjectCreateSerializer, SectionCreateSerializer


class SubjectListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.prefetch_related('sectionyear_set').all().filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubjectCreateSerializer
        elif self.request.method == 'GET':
            return SubjectViewSerializer


class SectionYearCreateAPI(CreateAPIView):
    queryset = SectionYear
    serializer_class = SectionCreateSerializer
    permission_classes = [IsAuthenticated]