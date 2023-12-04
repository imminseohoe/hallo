from django.contrib import admin

from . models import Article,HouseClick,ClickCount,UserProfile,Score

admin.site.register(Article)
admin.site.register(HouseClick)
admin.site.register(ClickCount)
admin.site.register(UserProfile)
admin.site.register(Score)