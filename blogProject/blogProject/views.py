# this file is made by me 
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')