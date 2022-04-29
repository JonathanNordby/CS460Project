from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from project import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'course', views.CourseView, 'course')
router.register(r'department', views.DepartmentView, 'department')
router.register(r'instructor', views.InstructorView, 'instructor')
router.register(r'prereq', views.PrereqView, 'prereq')
router.register(r'section', views.SectionView, 'section')
router.register(r'student', views.StudentView, 'student')
router.register(r'takes', views.TakesView, 'takes')
router.register(r'teaches', views.TeachesView, 'teaches')
router.register(r'func3f19', views.Func3F19View, 'func3f19')
router.register(r'func3f20', views.Func3F20View, 'func3f20')
router.register(r'func3s19', views.Func3S19View, 'func3s19')
router.register(r'func3s20', views.Func3S20View, 'func3s20')
router.register(r'func4f', views.Func4FView, 'func4f')
router.register(r'func4s', views.Func4SView, 'func4s')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
]