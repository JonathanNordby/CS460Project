from rest_framework import serializers
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

class Func3F19Serializer(serializers.ModelSerializer):
    class Meta:
        model = Func3F19
        fields = ('name', 'dept_name', 'studentcount')

class Func3F20Serializer(serializers.ModelSerializer):
    class Meta:
        model = Func3F20
        fields = ('name', 'dept_name', 'studentcount')

class Func3S19Serializer(serializers.ModelSerializer):
    class Meta:
        model = Func3S19
        fields = ('name', 'dept_name', 'studentcount')

class Func3S20Serializer(serializers.ModelSerializer):
    class Meta:
        model = Func3S20
        fields = ('name', 'dept_name', 'studentcount')

class Func4FSerializer(serializers.ModelSerializer):
    class Meta:
        model = Func4F
        fields = ('course_id', 'sec_id', 'sectionedstudents')

class Func4SSerializer(serializers.ModelSerializer):
    class Meta:
        model = Func4S
        fields = ('course_id', 'sec_id', 'sectionedstudents')

class Func5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Func5
        fields = ('concat_course_id_sec_id_field', 'name')