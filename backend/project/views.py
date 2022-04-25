from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project

# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
