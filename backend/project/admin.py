from django.contrib import admin
from .models import Project

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Project, TodoAdmin)