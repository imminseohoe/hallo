from django.contrib.auth.decorators import login_required
from mypage.models import UserProfile, Article, ClickCount,HouseClick, Score
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from mypage.forms import Form
from django.http import JsonResponse

@login_required
def ranking_kr(request, username):
    user = User.objects.get(username=username)
    top_click_counts = Score.objects.order_by('-score_count')[:30]
    score_count_obj, created = Score.objects.get_or_create(user=user)
    score_count = score_count_obj.score_count
    my_rank = Score.objects.filter(score_count__gt=score_count).count() + 1
    house_click = HouseClick.get_or_create()

    user_house = user.userprofile.house if user.userprofile and user.userprofile.house else ""
    house_attr = f"{user_house.lower()}_click" if user_house else ""
    my_house_click_count = getattr(house_click, house_attr, 0)


    pos_click  = house_click.poseidon_click

    att_click= house_click.athena_click

    app_click= house_click.apollo_click

    arr_click= house_click.artemis_click


    context = {
        'username': username,
        'click_count': score_count,
        'top_click_counts': top_click_counts,
        'my_rank': my_rank,
        'my_house_click_count': my_house_click_count,
        'pos_click': pos_click,
        'att_click': att_click,
        'app_click': app_click,
        'arr_click': arr_click,
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
        house_click = HouseClick.objects.first()
        if user.userprofile.house == 'Poseidon':
            house_click.poseidon_click += 1
        elif user.userprofile.house == 'Athena':
            house_click.athena_click += 1
        elif user.userprofile.house == 'Apollo':
            house_click.apollo_click += 1
        elif user.userprofile.house == 'Artemis':
            house_click.artemis_click += 1
        click_count_obj.save()
        house_click.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
@login_required
def update_socre(request, username):
    if request.method == 'POST':
        score = request.POST['score']
        user = request.user
        sum_score,created = Score.objects.get_or_create(user = user)
        score = int(score)
        sum_score.score_count += score
        sum = sum_score.score_count
        house_click = HouseClick.objects.first()
        if user.userprofile.house == 'Poseidon':
            house_click.poseidon_click += score
        elif user.userprofile.house == 'Athena':
            house_click.athena_click += score
        elif user.userprofile.house == 'Apollo':
            house_click.apollo_click += score
        elif user.userprofile.house == 'Artemis':
            house_click.artemis_click += score
        sum_score.save()
        house_click.save()
        return JsonResponse({'success': True})


        
@login_required
def mainpage(request, username):
    user = request.user
    userr = User.objects.get(username=username)
    click_count_obj, created = ClickCount.objects.get_or_create(user=userr)
    click_count = click_count_obj.click_count
    profile = UserProfile.objects.get(user=user)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('user_view')
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    
    context = {
        'user': user,
        'username' : username,
        'candy' : len(article_list),
        'click_count' : click_count
    }
    return render(request, 'mypage/kr/mainpage.html', context)

@login_required
def mypage_eg(request, username):
    user = request.user
    sum_score,created = Score.objects.get_or_create(user = user)    
    sum = sum_score.score_count
    #highest_score = 
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('user_view')
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)

    
    context = {
        'user': user,
        'username' : username,
        'candy' : len(article_list),
        'score' : sum,
       # 'highest_score' : highest_score,
    }
    return render(request, 'mypage/eg/mainpage_eg.html', context)

@login_required
def inside_pumpkin_eg(request, username,page_num):
    user = request.user
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    articles_per_page = 4
    start_index = (page_num - 1) * articles_per_page
    end_index = start_index + articles_per_page
    paginated_article_list = article_list[start_index:end_index]
    max_pages = (len(article_list) + articles_per_page - 1) // articles_per_page
    max_pages_minus_one = max_pages - 1
    if request.user.username == username:

        
        
        context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
        }
        return render(request, 'mypage/eg/inside_pumpkin_eg.html', context)
    else:
        japp_context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
        }
        return render(request, 'mypage/eg/inside_pumpkin_notme_eg.html', japp_context)
@login_required
def inside_pumpkin(request, username, page_num):
    user = request.user
    users = User.objects.get(username=username)
    article_list = Article.objects.filter(user=users)
    articles_per_page = 4
    start_index = (page_num - 1) * articles_per_page
    end_index = start_index + articles_per_page
    paginated_article_list = article_list[start_index:end_index]
    max_pages = (len(article_list) + articles_per_page - 1) // articles_per_page
    max_pages_minus_one = max_pages - 1
    if request.user.username == username:

        context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)

        }
        return render(request, 'mypage/kr/inside_pumpkin.html', context)
    else:
        japp_context = {
            'user': user,
            'username': username,
            'article_list': paginated_article_list,
            'max_pages': max_pages,
            'max_pages_minus_one': max_pages_minus_one,
            'range' : range(1,max_pages+1)
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
            user = request.user
            profile = UserProfile.objects.get(user=user)

            return redirect('mypage_eg', username)
    else:
        form = Form()
                                                                                                                                                        
    return render(request, 'write.html', {'form': form})
@login_required
def game(request, username):
    return render(request, 'mypage/eg/popup.html')
@login_required
def user_list(request, username):
    user = User.objects.get(username=username)
    article_list = Article.objects.filter(user=username)
    return render(request, 'list.html', {'article_list': article_list})


def user_view(request, username, num):
    try:
        article = Article.objects.get(id=num, user=User.objects.get(username=username))
        return render(request, 'view.html', {'article': article})
    except Article.DoesNotExist:    
        return redirect('user_list', username=username)