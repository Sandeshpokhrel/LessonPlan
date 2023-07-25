from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from .models import Subject, SectionYear


# Custom serializer for creating user.
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


# Serializer for sections:
class SectionSeializer(serializers.ModelSerializer):
    class Meta:
        model = SectionYear
        fields = ['year','section']

# Serializer for viewing subjects and sections:
class SubjectViewSerializer(serializers.ModelSerializer):
    sectionyear_set = SectionSeializer(many=True)
    class Meta:
        model = Subject
        fields = ['id', 'sub_name','sectionyear_set']
    queryset = Subject.objects.all()


# Serializer for creating subject.
class SubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'sub_name']


# serializer for creating section year.
class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionYear
        fields = ['year','section', 'subject']