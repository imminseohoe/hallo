from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from mypage.models import UserProfile
from django.contrib.auth.models import User

def molo(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        return redirect('mypage_kr', username=user.username)

    else:
        return redirect('user_view')
def ranking(request):
    user = User.objects.get(username=request.user.username)
    
    return render(request, 'ranking.html', {'username': user.username})