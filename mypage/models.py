from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=[('en', 'English'), ('ko', '한국어')],default='eg')
    house = models.CharField(max_length=100, null=True)  

class Article(models.Model):
    name = models.CharField(max_length=10)
    contents = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.name

class ClickCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    click_count = models.IntegerField(default=0)
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    socre_count = models.IntegerField(default=0)


class HouseClick(models.Model):
    apollo_click = models.IntegerField(default=0)
    athena_click = models.IntegerField(default=0)
    poseidon_click = models.IntegerField(default=0)
    artemis_click = models.IntegerField(default=0)

    @classmethod
    def get_or_create(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "House Click Counts"