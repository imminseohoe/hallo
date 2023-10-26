from django.contrib.auth.decorators import login_required
from mypage.models import UserProfile, Article, ClickCount
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from mypage.forms import Form

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from .models import ClickCount
@login_required
def ranking_kr(request, username):
    user = User.objects.get(username=username)
    click_count_obj, created = ClickCount.objects.get_or_create(user=user)
    click_count = click_count_obj.click_count
    context = {
        'username': username,
        'click_count': click_count
    }
    return render(request, 'mypage/kr/ranking.html', context)
    
def get_click_count(request, username):
    user = User.objects.get(username=username)
    click_count_obj, created = ClickCount.objects.get_or_create(user=user)
    click_count = click_count_obj.click_count
    return render(request, 'mypage/kr/click_count.html', {'click_count': click_count})
@login_required
def update_click_count(request, username):
    if request.method == 'POST':
        user = request.user
        click_count_obj, created = ClickCount.objects.get_or_create(user=user)
        click_count_obj.click_count += 1
        click_count_obj.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
@login_required
def mainpage(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('user_view')

    context = {
        'user': user,
        'username' : username,
        
    }
    return render(request, 'mypage/kr/mainpage.html', context)

@login_required
def mypage_eg(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('user_view')

    context = {
        'user': user,
        'username' : username,
    }
    return render(request, 'mypage/eg/mainpage_eg.html', context)

@login_required
def inside_pumpkin(request, username):
    if request.user.username == username:
        user = request.user
        users = User.objects.get(username=username)
        article_list = Article.objects.filter(user=users)
        context = {
            'user': user,
            'username' : username,
            'article_list' : article_list
        }
        return render(request, 'mypage/kr/inside_pumpkin.html', context)
    else:
        japp_context ={
            'username' : username,
            'article_list': Article.objects.filter(user=User.objects.get(username=username))
        }
        
        return render(request, 'mypage/kr/inside_pumpkin_notme.html', japp_context)
@login_required
def write(request, username):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = User.objects.get(username=username)
            article.save()
            return redirect('inside_pumpkin', username=username)
    else:
        form = Form()
                                                                                                                                                        
    return render(request, 'write.html', {'form': form})

@login_required
def user_list(request, username):
    user = User.objects.get(username=username)
    article_list = Article.objects.filter(user=user)
    return render(request, 'list.html', {'article_list': article_list})

@login_required
def user_view(request, username, num):
    try:
        article = Article.objects.get(id=num, user=User.objects.get(username=username))
        return render(request, 'view.html', {'article': article})
    except Article.DoesNotExist:
        return redirect('user_list', username=username)