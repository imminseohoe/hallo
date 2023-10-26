from django import forms

class ChangeUsernameForm(forms.Form):
    name = forms.CharField(label='이름을 입력하세요', max_length=10)
    choose_lang = forms.ChoiceField(label='언어 선택', choices=[('en', '영어'), ('ko', '한국어')])