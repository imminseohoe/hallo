
from django.contrib import admin
from django.urls import path, include
from mypage import views
from .views import mainpage, inside_pumpkin,ranking_kr

urlpatterns = [
    path('<str:username>/update_click_count/', views.update_click_count, name='update_click_count'),
    path('<str:username>/ranking/', views.ranking_kr, name='ranking_kr'),
    path('<str:username>/click_count/', views.get_click_count, name='click_count'),
    path('<str:username>/', views.mainpage, name='mypage_kr'),
    path('kr/<str:username>/inside_pumpkin/<int:page_num>/', views.inside_pumpkin, name='inside_pumpkin'),
    path('<str:username>/write/', views.write, name='write'),
    path('kr/<str:username>/inside_pumpkin/view/<int:num>/', views.user_view, name='user_view'),
    path('eg/<str:username>/inside_pumpkin/view/<int:num>/',views.user_view, name='user_view' ),
    path('<str:username>/list/', views.user_list, name='user_list'),
    path('eg/<str:username>/inside_pumpkin/<int:page_num>/  ', views.inside_pumpkin_eg, name='inside_pumpkin_eg'),
    path('<str:username>/eg/', views.mypage_eg, name='mypage_eg'),
    path('<str:username>/game/', views.game, name= 'game'),
    path('<str:username>/update_score/', views.update_socre, name= 'update_socre'),
]
