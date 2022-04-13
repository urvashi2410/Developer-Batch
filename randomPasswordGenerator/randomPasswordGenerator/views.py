# this file is user defined 

# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def password(request):
    return render(request, 'password.html')

def contact(request):
    return render(request, 'contact.html')