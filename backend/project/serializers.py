from rest_framework import serializers
from .models import (
    Project,
    Course,
    Department,
    Instructor,
    Prereq,
    Section,
    Student,
    Takes,
    Teaches,
)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'completed')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'title', 'dept_name', 'credits')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('dept_name', 'building', 'budget')

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id', 'name', 'dept_name', 'salary')

class PrereqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prereq
        fields = ('course', 'prereq')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('course', 'sec_id', 'semester', 'year', 'building', 'room', 'capacity')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'dept_name', 'total_credits')

class TakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takes
        fields = ('dbid', 'course', 'sec', 'semester', 'year', 'grade')

class TeachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaches
        fields = ('course', 'sec', 'semester', 'year', 'dbid')
