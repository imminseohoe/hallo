
from django.contrib import admin
from django.urls import path, include
from mypage import views
from .views import mainpage, inside_pumpkin

urlpatterns = [

    path('<str:username>/', mainpage, name='mypage'),
    path('<str:username>/inside_pumpkin/', inside_pumpkin, name='inside_pumpkin'),
    path('<str:username>/write/', views.write, name='write'),
    path('<str:username>/view/<int:num>/', views.user_view, name='user_view'),
    path('<str:username>/list/', views.user_list, name='user_list'),
]
