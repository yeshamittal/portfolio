from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'all_blogs.html', {"blogs": blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'details.html', {'blog': blog})