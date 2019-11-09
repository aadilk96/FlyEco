from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'aadilk',
#         'title' : 'Blog Post 1', 
#         'content': 'First',
#         'date_posted': 'Nov 9, 2019'
#     },
#     {
#         'author': 'test',
#         'title' : 'Blog Post 2', 
#         'content': 'Second',
#         'date_posted': 'Nov 9, 2019'
#     }
# ]

def home(request): 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'flyeco/home.html', context)

def about(request): 
    return render(request, 'flyeco/about.html', {'title':'About'}) 

def search(request): 
    return render(request, 'flyeco/search.html', {'title':'Search'}) 