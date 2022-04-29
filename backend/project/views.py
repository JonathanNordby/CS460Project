from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    CourseSerializer,
    DepartmentSerializer,
    InstructorSerializer,
    PrereqSerializer,
    SectionSerializer,
    StudentSerializer,
    TakesSerializer,
    TeachesSerializer,
    Func3F19Serializer,
    Func3F20Serializer,
    Func3S19Serializer,
    Func3S20Serializer,
    Func4FSerializer,
    Func4SSerializer,
)
from .models import (
    Course,
    Department,
    Instructor,
    Prereq,
    Section,
    Student,
    Takes,
    Teaches,
    Func3F19,
    Func3F20,
    Func3S19,
    Func3S20,
    Func4F,
    Func4S,
)

# Create your views here.

class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class InstructorView(viewsets.ModelViewSet):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class PrereqView(viewsets.ModelViewSet):
    serializer_class = PrereqSerializer
    queryset = Prereq.objects.all()

class SectionView(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TakesView(viewsets.ModelViewSet):
    serializer_class = TakesSerializer
    queryset = Takes.objects.all()

class TeachesView(viewsets.ModelViewSet):
    serializer_class = TeachesSerializer
    queryset = Teaches.objects.all()

class Func3F19View(viewsets.ModelViewSet):
    serializer_class = Func3F19Serializer
    queryset = Func3F19.objects.all()

class Func3F20View(viewsets.ModelViewSet):
    serializer_class = Func3F20Serializer
    queryset = Func3F20.objects.all()

class Func3S19View(viewsets.ModelViewSet):
    serializer_class = Func3S19Serializer
    queryset = Func3S19.objects.all()

class Func3S20View(viewsets.ModelViewSet):
    serializer_class = Func3S20Serializer
    queryset = Func3S20.objects.all()

class Func4FView(viewsets.ModelViewSet):
    serializer_class = Func4FSerializer
    queryset = Func4F.objects.all()

class Func4SView(viewsets.ModelViewSet):
    serializer_class = Func4SSerializer
    queryset = Func4S.objects.all()
