
from django.contrib import admin
from django.urls import path, include
from community.views import molo, ranking


urlpatterns = [
    path('', molo, name='molo'),
    path('admin/', admin.site.urls, name="admin"),
    path('ginlo/', include('ginlo.urls')),
    path('accounts/',include('allauth.urls')),
    path('mypage/', include('mypage.urls')),
    path('ranking/', ranking, name="ranking")

]
