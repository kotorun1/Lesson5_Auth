from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    students = models.ManyToManyField('Student')

    def __str__(self):
        return str(self.year_of_study) + self.name

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    lessons = models.ManyToManyField('Lesson')

    def __str__(self):
        return self.fullname

class Lesson(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

