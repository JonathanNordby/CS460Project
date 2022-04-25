from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from project import views

router = routers.DefaultRouter()
router.register(r'project', views.ProjectView, 'project')
router.register(r'course', views.CourseView, 'course')
router.register(r'department', views.DepartmentView, 'department')
router.register(r'instructor', views.InstructorView, 'instructor')
router.register(r'prereq', views.PrereqView, 'prereq')
router.register(r'section', views.SectionView, 'section')
router.register(r'student', views.StudentView, 'student')
router.register(r'takes', views.TakesView, 'takes')
router.register(r'teaches', views.TeachesView, 'teaches')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
]