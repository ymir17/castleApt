from django.contrib.auth import logout
from django.shortcuts import render, redirect


def index(request):
    logout(request)
    return redirect('home-index')
