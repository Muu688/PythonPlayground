from re import template
from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView): # Gets data from Model
    model = Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView): # Renders Template without getting data from Model
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('datecreated')
    template_name = 'index.html'