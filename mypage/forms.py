from django.forms import ModelForm, TextInput,Textarea
from mypage.models import Article

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'contents']
        widgets = {
            'name': TextInput(attrs={
                'class': "name_class",
                'style': 'max-width: 1000px;',
                'placeholder': 'name'
                }),
            'contents': Textarea(attrs={
                "class": "contents_class",
                'placeholder': 'contents'
                })
            }
        