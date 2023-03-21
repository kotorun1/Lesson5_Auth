from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class ClassView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ClassDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAdminUser]

class StudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

class LessonView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LessonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]

