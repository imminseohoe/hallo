from django.urls import path
from . import views

urlpatterns = [
    path('', views.ginlo, name='user_view')
]