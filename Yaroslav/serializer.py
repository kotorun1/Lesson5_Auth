from rest_framework import serializers
from .models import *

class ClassSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Class
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'






