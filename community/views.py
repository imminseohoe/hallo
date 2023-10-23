from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from mypage.models import UserProfile
from django.contrib.auth.models import User

def molo(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        return redirect('mypage', username=user.username)

    else:
        return redirect('user_view')