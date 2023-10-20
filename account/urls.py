
from django.contrib import admin
from django.urls import path, include
from account import views


urlpatterns = [
    path('accounts/',include('allauth.urls')),
    path('login/', views.login, name = 'login')
]
