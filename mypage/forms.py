from django.forms import ModelForm
from mypage.models import Article

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'contents']
