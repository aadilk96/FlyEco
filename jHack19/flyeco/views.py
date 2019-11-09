from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Post
from . import query


def home(request): 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'flyeco/home.html', context)

def about(request): 
<<<<<<< HEAD
    return render(request, 'flyeco/about.html', {'title':'About'}) 

def search(request):
    if request.method == "POST":
        f = query.SimpleForm(request.POST)
        if f.is_valid():
            destination = f.cleaned_data.get("destination")
            departure = f.cleaned_data.get("departure")
            date_depart = f.cleaned_data.get("date_depart")
            date_arrive = f.cleaned_data.get("date_arrive")
            return render(request, 'flyeco/results.html', {'destination': destination, 'date': d})
    else:
        f = query.SimpleForm()
    return render(request, 'flyeco/search.html', {'title':'Search', 'form': f}) 
=======
    return render(request, 'flyeco/about.html', {'title':'About'})
>>>>>>> 9a556603b9bdca94646abd9df41f74048ec0bb6d
