from django import forms

class ChangeUsernameForm(forms.Form):
    name = forms.CharField(label='write your name', max_length=10)
    choose_lang = forms.ChoiceField(label='choose yout language', choices=[('en', 'English'), ('ko', '한국어')])