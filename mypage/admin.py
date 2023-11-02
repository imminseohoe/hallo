from django.contrib import admin

from . models import Article,HouseClick,ClickCount

admin.site.register(Article)
admin.site.register(HouseClick)
admin.site.register(ClickCount)