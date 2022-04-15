# this file is user defined 

from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    # return HttpResponse("This is home page")
    return render(request, 'index.html')

def password(request):
    choice = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('passwordlength'))
    isUpper = request.GET.get('uppercase')
    isNumber = request.GET.get('number')
    isSymbol = request.GET.get('symbol')

    if isUpper == 'on':
        choice.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if isNumber == 'on':
        choice.extend(list('0123456789'))
    if isSymbol == 'on':
        choice.extend(list('''!@#$%^&*()_'''))
    
    mypassword = ""

    for i in range(length):
        choose = random.choice(choice)
        mypassword += choose
    
    data = {
        'password' : mypassword,
        'class' : "third year",
        'address' : "sant nagar"
    }
    
    return render(request, 'password.html', data)

def contact(request):
    return render(request, 'contact.html')