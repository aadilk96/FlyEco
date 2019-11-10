from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile

def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for %s" % {username})
            return redirect('login')
    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user_points = request.user.profile.points
    leaderBoard = [{"username": x.user.username, "points": x.points}
                   for x in Profile._meta.model.objects.all()]
    leaderBoard = sorted(leaderBoard, key=lambda i: i['points'], reverse=True)
    return render(request, 'users/profile.html', {"user_point": user_points, 'leaderBoard': leaderBoard})