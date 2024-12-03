# 
from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",  # API nomi
        default_version='v1',   # API versiyasi
        description="API for managing teachers, courses, news, and feedback. Provides authentication (login/register) functionalities.",  # API tavsifi
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),  # Kontakt ma'lumotlari
        license=openapi.License(name="BSD License"),  # Litsenziya
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # API uchun umumiy ruxsat
)

# API endpointlar
urlpatterns = [
    # Teacher endpoints
    path('teachers/', TeacherCreateListView.as_view(), name='teacher-list'),  # Teacher List and Create
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),  # Teacher Detail (Retrieve, Update, Delete)
    
    # News endpoints
    path('news/list/', NewsCreateListView.as_view(), name='news-list'),  # News List
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),  # News Detail (Retrieve, Update, Delete)

    # Course endpoints
    path('courses/', CurseCreateListView.as_view(), name='course-list'),  # Course List and Create
    path('courses/<int:pk>/', CurseDetailView.as_view(), name='course-detail'),  # Course Detail (Retrieve, Update, Delete)

    # Feedback endpoints
    path('feedback/list/', FeedbackCreateListView.as_view(), name='feedback-list'),  # Feedback List
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),  # Feedback Detail (Retrieve, Update, Delete)

    # Authentication endpoints
    path('log_in/', log_in, name='log-in'),  # Log in
    path('log_out/', log_out, name='log-out'),  # Log out
    path('register/', register, name='register'),  # Register new user
    path('say_hello/', say_hello, name='say-hello'),  # Test authentication

    # Swagger documentation endpoints
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc UI
]
