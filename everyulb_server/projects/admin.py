from django.contrib import admin

# Register your models here.
from .models import Project, ProjectType

admin.site.register(Project)
admin.site.register(ProjectType)