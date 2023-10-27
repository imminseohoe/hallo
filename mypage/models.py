from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('en', 'English'), ('ko', '한국어')], default='en')

class Article(models.Model):
    name = models.CharField(max_length=10)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=100)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ClickCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE,)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.house.name}"