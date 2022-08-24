from django.contrib import admin
from .models import Blog  # must import from models folder

# Register your models here.
admin.site.register(Blog)  # adds the model 'Project' into Django admin
