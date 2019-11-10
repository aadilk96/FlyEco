from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Post
from . import query
from . import skyscanner_integration

from users.models import Profile

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


def home(request):
    if request.method == "POST":
        f = query.SimpleForm(request.POST)
        if f.is_valid():
            destination = f.cleaned_data.get("destination")
            departure = f.cleaned_data.get("departure")
            date_depart = f.cleaned_data.get("date_depart")
            date_return = f.cleaned_data.get("date_return")
            #call to api methods
            data = skyscanner_integration.handle_query(
                destination, departure, date_depart, date_return)
            leaderBoard = [{"username": x.user.username, "points": x.points}
                           for x in Profile._meta.model.objects.all()]
            leaderBoard = sorted(
                leaderBoard, key=lambda i: i['points'], reverse=True)
            try:
                user_points = request.user.profile.points
            except Exception:
                user_points = 0
            return render(request, 'flyeco/results.html', {'destination': destination, 'deets': data, 'leaderBoard': leaderBoard, 'user_point': user_points})
    else:
        f = query.SimpleForm()
    leaderBoard = [{"username": x.user.username, "points": x.points}
                   for x in Profile._meta.model.objects.all()]
    leaderBoard = sorted(leaderBoard, key=lambda i: i['points'], reverse=True)
    try:
        user_points = request.user.profile.points
    except Exception:
        user_points = 0
    print("The user points is", user_points)
    return render(request, 'flyeco/home.html', {'form': f, 'leaderBoard': leaderBoard, 'user_point': user_points})


def increasePoints(request, pts):
    from twilio.rest import Client
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC90ecfcae0dba57ce05ff3ea8c6d57942'
    auth_token = '2c0c401ca65a5427344f3a6d4f575952'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Whadup Henooooooochi!',
        from_='+12053418399',
        to='+4915226542018'
    )
    print(message.sid)
    print("Got points", pts)
    if request.method == "POST":
        setattr(request.user.profile, "points",
                request.user.profile.points + pts)
        request.user.save()
    return redirect('flyeco-home')


def about(request):
    return render(request, 'flyeco/about.html', {'title': 'About'})
