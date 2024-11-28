from rest_framework.serializers import ModelSerializer

from core.models import *

class TeacherListSerializer(ModelSerializer):
    class Meta:
        model = Teacher  
        fields = '__all__'  

class TeacherDetailSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields =['id', 'name', ]

class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'name',]

class CurseCreatelistSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseDetailSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title',]


class FeedbackCreateSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['user_name', 'user_email', 'content',]


class FeedbackDetailSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


