from django.contrib import admin
from .models import Project  # must import from models folder

# Register your models here.
admin.site.register(Project)  # adds the model 'Project' into Django admin
