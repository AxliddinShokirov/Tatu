from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication  import TokenAuthentication
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import (api_view,
 authentication_classes,
 permission_classes,)



class TeacherCreateListView(generics.ListCreateAPIView):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()
    
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()

class NewsCreateListView(generics.ListCreateAPIView):
    serializer_class = NewsListSerializer
  
    def get_queryset(self):
        return News.objects.order_by('-id')[:1]

    def perform_create(self, serializer):
        serializer.save()

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()

class CurseCreateListView(generics.ListCreateAPIView):
    serializer_class = CurseCreatelistSerializer
    queryset = Course.objects.all()
    
class CurseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    
class FeedbackCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackCreateSerializer
    queryset = Feedback.objects.all()

class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackDetailSerializer
    queryset = Feedback.objects.all()





@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token_key , _ = Token.objects.get_or_create(username=user)
        context = {
            'success' : True,
            'username': user.username,
            'key' : token_key.key
        }      

    else:
        context = {
            'success' : False,
            'error' : 'Invalid credentials.'
        }
    return Response(context)
  
@api_view(['POST'])
def log_out(request):
    token = request.data.get('token')
    if token is not None:
        try:
            token_key = Token.objects.get(key=token)
            token_key.delete()
            context = {
                'success' : True,
                'message' : 'Token deleted successfully.'
            }
        except:
            context = {
                'success' : False,
                'error' : 'Invalid token.'
            }
    else:
        context = {
            'success' : False,
            'error' : 'No token provided.'
        }
    return Response(context)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def say_hello(request):
    return Response('Hello, World!')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def log_out(request):
    Token.objects.get(user=request.user).delete()
    return Response({'success':True})


@api_view(['POST'])  
def register(request):
    try:
       
        username = request.data.get('username')
        password = request.data.get('password')
        
  
        user = User.objects.create(username=username,
                                    password=password)
        token = Token.objects.create(user=user)
      
        context = {
            'success': True,
            'username': user.username,
            'password': password, 
            'id': user.id,
            'token' : token.key
        }
    except Exception as e:

        context = {
            'success': False,
            'error': str(e), 
        }

    return Response(context)
