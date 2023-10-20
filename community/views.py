
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def molo(request):
    return render(request, 'hhh.html')
    
