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