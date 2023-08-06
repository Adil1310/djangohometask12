from django.shortcuts import render
from .models import User

# Create your views here.

def count_users():
    return User.objects.count()