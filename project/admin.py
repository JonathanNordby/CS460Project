from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(DBDepartment)
admin.site.register(DBCourse)
admin.site.register(DBCourseOffering)
admin.site.register(DBDegreeProgram)
admin.site.register(DBStudent)
admin.site.register(DBSchedule)
admin.site.register(DBAdvisor)
admin.site.register(DBAdvisorCode)
admin.site.register(DBComment)

admin.site.register(DBUser)