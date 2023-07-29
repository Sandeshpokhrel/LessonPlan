from rest_framework import serializers

from .models import User, SectionYear, Subject


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
        fields = ['id', 'sub_name','user']



# serializer for creating section year.
class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionYear
        fields = ['year','section', 'subject']