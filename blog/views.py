# try and get an object, if none then show 404 page
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def all_blogs(request):
    # blogs = Blog.objects.all()
    # most current blogs will show on top
    # limits the amount of blogs showing (set to 2)
    # blogs = Blog.objects.order_by('-date')[:2]
    blogs = Blog.objects.order_by('-date')

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    # grab a particular object, if unable then display 404 page
    # pk is short for primary key (ID# in database)
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
