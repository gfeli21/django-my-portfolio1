from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Begin adding more paths for web development such as home page.
    path('', views.all_blogs, name='all_blogs'),  # Blog home page
    path('<int:blog_id>/', views.detail, name='detail'),  # Show blog posts

]
