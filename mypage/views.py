from django.contrib.auth.decorators import login_required
from mypage.models import UserProfile, Article
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from mypage.forms import Form


@login_required
def mainpage(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 유저가 존재하지 않을 때 처리할 내용
        # 예를 들어 404 에러를 반환하거나 다른 처리를 할 수 있습니다.
        raise Http404("해당 유저를 찾을 수 없습니다.")

    context = {
        'user': user,
        'username' : username,
    }
    return render(request, 'mypage/mainpage.html', context)

@login_required
def inside_pumpkin(request, username):
    user = request.user
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    context = {
        'user': user,
        'username' : username,
        'article_list' : article_list

    }
    return render(request, 'mypage/inside_pumpkin.html', context)

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