from django.shortcuts import render
from .models import Post    
from django.views.generic import ListView

# Create your views here.
class HomePage(ListView):
    http_method_names=["get"]
    template_name="feed/Homepage.html"
    model=Post
    context_object_name="posts"
    queryset=Post.objects.all().order_by("-id")[0:30]
