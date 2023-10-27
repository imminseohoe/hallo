from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from mypage.models import UserProfile
from django.contrib.auth.models import User

@login_required
def molo(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
        language = profile.language

        if language == 'ko':
            return redirect('mypage_kr', username=user.username)
        else:
            return redirect('mypage_eg', username=user.username)

    except UserProfile.DoesNotExist:
        return redirect('user_view')
