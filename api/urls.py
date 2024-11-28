from django.urls import path
from .views import  *

urlpatterns = [
    path('teachers/',TeacherCreateListView.as_view() ),  # List and Create
    path('teachers/<int:pk>/',TeacherDetailView.as_view() ),  # Retrieve, Update, Delete
    path('news/list', NewsCreateListView.as_view() ),
    path('news/<int:pk>/', NewsDetailView.as_view()),
    path('news/<int:pk>,', NewsDetailView.as_view()), 
    path('courses/', CurseCreateListView.as_view() ),
    path('courses/<int:pk>/', CurseDetailView.as_view()),
    path('feedback/list/', FeedbackCreateListView.as_view()),  # Retrieve, Update, Delete
    path('log_in/', log_in) , 
    path('log_out/', log_out) ,
    path( 'register/', register),
    path('say_hello/', say_hello) ,
]
