from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ChangeUsernameForm
from mypage.models import UserProfile
def ginlo(request):
    return render(request, 'ginlo/ginlo.html')

@login_required
def choose_name(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['name']
            lang_choose = form.cleaned_data['choose_lang']
            try:
                user_profile = request.user.userprofile
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=request.user)

            user_profile.language = lang_choose
            user_profile.save()

            user = request.user
            user.username = new_username
            user.save()

            if request.user.email.endswith('@stpaulhanoi.com'):
                return redirect('house')
            elif lang_choose == "ko":
                return redirect('mypage_kr', user)
            else:
                return redirect('mypage_eg', user)
    else:
        form = ChangeUsernameForm()

    return render(request, 'ginlo/choose.html', {'form': form})

@login_required
def house(request):
    if request.method == 'POST':
        house_choice = request.POST.get('house')
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.house = house_choice
        user_profile.save()

        lang_choose = user_profile.language
        user = request.user

        if lang_choose == "ko":
            return redirect('mypage_kr', user)
        else:
            return redirect('mypage_eg', user)        

    return render(request, 'ginlo/house.html')