from rest_framework import serializers

from .models import User, SectionYear, Subject, Topic, Chapter, Assignment, Resource


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username','password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


# Serializer for sections:
class SectionSeializer(serializers.ModelSerializer):
    class Meta:
        model = SectionYear
        fields = ['id', 'section']

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
        fields = ['id', 'sub_name','user']



# serializer for creating section year.
class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionYear
        fields = ['id','section', 'subject']


# serializer for viewing Topics.
class TopicViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic_name']


# serializer for viewing assignment
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'assign_name','file','chapter']


# serializer for viewing resources. 
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource 
        fields = ['id', 'res_name','file','chapter']


# serializer for viewing Chpater and topic.
class ChapterViewSerializer(serializers.ModelSerializer):
    topic_set = TopicViewSerializer(many=True) 
    assignment_set = AssignmentSerializer(many=True)
    resource_set = ResourceSerializer(many=True)
    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name', 'section_year', 'topic_set','assignment_set','resource_set']


# serializer for creating chapters.
class ChapterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name','section_year']


# serializer for creating topics.
class TopicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'topic_name', 'chapter']