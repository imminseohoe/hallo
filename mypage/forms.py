from django.forms import ModelForm, TextInput,Textarea
from mypage.models import Article
from django import forms

class NameSetupForm(forms.Form):
    name = forms.CharField(label='이름', max_length=100)
class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'contents']
        widgets = {
            '': TextInput(attrs={
                'class': "name_class",
                'style': 'max-width: 1000px;',
                'placeholder': 'name'
                }),
            '': Textarea(attrs={
                "class": "contents_class",
                'placeholder': 'contents'
                })
            }
        