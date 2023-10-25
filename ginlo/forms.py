from django import forms

class ChangeUsernameForm(forms.Form):
    name = forms.CharField(label='이름을 입력하세요', max_length=10)