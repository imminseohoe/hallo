from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ChangeUsernameForm
from mypage.models import UserProfile
from django.contrib.auth.models import User

def ginlo(request):
    return render(request, 'ginlo/ginlo.html')

@login_required
def choose_name(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['name']
            try:
                user = User.objects.get(username=request.user.username)
                user.username = new_username
                user.save()
                return redirect('mypage', user)
            except User.DoesNotExist:
                return redirect('user_view')
    else:
        form = ChangeUsernameForm()

    return render(request, 'ginlo/choose.html', {'form': form})