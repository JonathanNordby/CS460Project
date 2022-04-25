from django.contrib import admin
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

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'dept_name', 'credits')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'building', 'budget')

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept_name', 'salary')

class PrereqAdmin(admin.ModelAdmin):
    list_display = ('course', 'prereq')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('course', 'sec_id', 'semester', 'year', 'building', 'room', 'capacity')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept_name', 'total_credits')

class TakesAdmin(admin.ModelAdmin):
    list_display = ('dbid', 'course', 'sec', 'semester', 'year', 'grade')

class TeachesAdmin(admin.ModelAdmin):
    list_display = ('course', 'sec', 'semester', 'year', 'dbid')

# Register your models here.

admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Prereq, PrereqAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Takes, TakesAdmin)
admin.site.register(Teaches, TeachesAdmin)
