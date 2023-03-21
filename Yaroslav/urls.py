from django.urls import path,include, re_path
from .views import *
urlpatterns = [
    path('classes/', ClassView.as_view()),
    path('classes/<int:pk>/', ClassDetailView.as_view()),
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('lessons/', LessonView.as_view()),
    path('lessons/<int:pk>/', LessonDetailView.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('djoser/', include('djoser.urls')),
    re_path(r'^djoser/', include('djoser.urls.authtoken')),
]
