from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import viewsets, permissions
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
    Func5Serializer,
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
    Func5,
)

class CustomPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Reject if not authenticated
        if request.auth is None:
            return False

        # Instructor is used in F1, F2
        if view.basename == 'instructor':
            # Only allow if user is in the admin group
            return request.user.groups.filter(name='Admin').exists()

        # func3 is used in F3
        if view.basename in ['func3f19', 'func3s19', 'func3f20', 'func3s20']:
            # Only allow if user is in the admin group
            return request.user.groups.filter(name='Admin').exists()
        
        # func4 is used in F4
        if view.basename in ['func4f', 'func4s']:
            # Only allow if user is in the professors group
            return request.user.groups.filter(name='Professors').exists()

        # func5 is used in F5
        if view.basename == 'func5':
            # Only allow if user is in the professors group
            return request.user.groups.filter(name='Professors').exists()

        # course is used in F6
        if view.basename == 'course':
            # Only allow if user is in the students group
            return request.user.groups.filter(name='Students').exists()

        # Otherwise, reject
        return False

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [CustomPermissions]
    queryset = Course.objects.all()

class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [CustomPermissions]
    queryset = Department.objects.all()

class InstructorView(viewsets.ModelViewSet):
    serializer_class = InstructorSerializer
    permission_classes = [CustomPermissions]
    queryset = Instructor.objects.all()

class PrereqView(viewsets.ModelViewSet):
    serializer_class = PrereqSerializer
    permission_classes = [CustomPermissions]
    queryset = Prereq.objects.all()

class SectionView(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    permission_classes = [CustomPermissions]
    queryset = Section.objects.all()

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [CustomPermissions]
    queryset = Student.objects.all()

class TakesView(viewsets.ModelViewSet):
    serializer_class = TakesSerializer
    permission_classes = [CustomPermissions]
    queryset = Takes.objects.all()

class TeachesView(viewsets.ModelViewSet):
    serializer_class = TeachesSerializer
    permission_classes = [CustomPermissions]
    queryset = Teaches.objects.all()

class Func3F19View(viewsets.ModelViewSet):
    serializer_class = Func3F19Serializer
    permission_classes = [CustomPermissions]
    queryset = Func3F19.objects.all()

class Func3F20View(viewsets.ModelViewSet):
    serializer_class = Func3F20Serializer
    permission_classes = [CustomPermissions]
    queryset = Func3F20.objects.all()

class Func3S19View(viewsets.ModelViewSet):
    serializer_class = Func3S19Serializer
    permission_classes = [CustomPermissions]
    queryset = Func3S19.objects.all()

class Func3S20View(viewsets.ModelViewSet):
    serializer_class = Func3S20Serializer
    permission_classes = [CustomPermissions]
    queryset = Func3S20.objects.all()

class Func4FView(viewsets.ModelViewSet):
    serializer_class = Func4FSerializer
    permission_classes = [CustomPermissions]
    queryset = Func4F.objects.all()

class Func4SView(viewsets.ModelViewSet):
    serializer_class = Func4SSerializer
    permission_classes = [CustomPermissions]
    queryset = Func4S.objects.all()

class Func5View(viewsets.ModelViewSet):
    serializer_class = Func5Serializer
    permission_classes = [CustomPermissions]
    queryset = Func5.objects.all()
