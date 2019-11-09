from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    return render(request, 'flyeco/home.html')

def about(request): 
    return render(request, 'flyeco/about.html', {'title':'About'}) 