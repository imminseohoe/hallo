from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    bio = models.TextField(default="")  # 기본값을 빈 문자열로 설정

    # 추가 정보 필드들을 정의합니다
    # ...

    def __str__(self):
        return self.user.username