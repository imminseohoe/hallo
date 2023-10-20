from django.forms import ModelForm
from community.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)  # 추가 정보 필드들을 포함시킵니다