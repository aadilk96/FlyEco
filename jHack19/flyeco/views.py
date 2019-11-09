from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Post
from . import query
from . import skyscanner_integration


deets = [
        {
            "from": "PARIS",
            "to": "BREMEN",
            "depart_date": "2019.10.21",
            "return_date": "2019.10.27",
            "price": "218",
            "carbon": "125"
        },
        {
            "from": "PARIS",
            "to": "BREMEN",
            "depart_date": "2019.10.21",
            "return_date": "2019.10.27",
            "price": "276",
            "carbon": "136"
        },
        {
            "from": "PARIS",
            "to": "BREMEN",
            "depart_date": "2019.10.21",
            "return_date": "2019.10.27",
            "price": "276",
            "carbon": "147"
    }
]

def about(request): 
    return render(request, 'flyeco/about.html', {'title':'About'}) 

def home(request): 
    if request.method == "POST":
        f = query.SimpleForm(request.POST)
        if f.is_valid():
            destination = f.cleaned_data.get("destination")
            departure = f.cleaned_data.get("departure")
            date_depart = f.cleaned_data.get("date_depart")
            date_return = f.cleaned_data.get("date_return")
            #call to api methods
            data = skyscanner_integration.handle_query(destination,departure,date_depart,date_return)
            return render(request, 'flyeco/results.html', {'destination': destination, 'deets': data})
    else:
        f = query.SimpleForm()
    return render(request, 'flyeco/search.html', {'title':'Search', 'form': f}) 
