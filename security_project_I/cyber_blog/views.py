from django.shortcuts import render
from .models import Post

def home (request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'cyber_blog/home.html', context)

def about (request):
    return render(request, 'cyber_blog/about.html', {'title': 'About'})

