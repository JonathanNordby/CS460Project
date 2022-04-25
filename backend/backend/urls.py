from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from project import views

router = routers.DefaultRouter()
router.register(r'project', views.ProjectView, 'project')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
]