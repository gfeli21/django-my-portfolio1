from django.shortcuts import render
from .models import Project  # to help pass info from views to templates
# Create your views here.


def home(request):
    projects = Project.objects.all()  # grabs all project objects from db
    # grabs everything out of db, turns them into Python objects and puts them in a list.
    return render(request, 'portfolio/home.html', {'projects': projects})
