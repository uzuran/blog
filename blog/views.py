from django.shortcuts import render
from .models import Post
posts = [
    {
        'author': 'uzuran',
        'title': 'Nohejbal',
        'content': 'Přátele, dnes se uspořáda nohec tak jak ho prostě máme rádi :)',
        'date_posted': 'útrery 1.září'
    },

    {
        'author': 'Láďa',
        'title': 'Nohejbal',
        'content': 'Přátele, dnes se to ruší :)',
        'date_posted': 'útrery 1.září'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def map(request):
    return render(request, 'blog/map.html', {'title': 'Map'})
