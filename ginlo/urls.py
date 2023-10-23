from django.urls import path
from . import views

urlpatterns = [
    path('', views.ginlo, name='user_view'),
    path('choose_name/', views.choose_name, name='choose_name'),
]