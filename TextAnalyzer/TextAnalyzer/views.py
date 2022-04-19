# from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    return render(request, 'home.html')

def ans(request):
    if request.method == 'POST':
        text = request.POST.get('textarea')
    length = len(text)
    wordsList = text.split()
    noOfWords = len(wordsList)
    symbols = list('''~!@#$%^&*'(){}:";'[]\|`''')
    
    countUpperCase = 0
    countLowerCase = 0
    countNumbers = 0
    countSymbols = 0

    for i in text:
        if i.isupper():
            countUpperCase += 1
        if i.islower():
            countLowerCase += 1
        if i.isnumeric():
            countNumbers += 1
        if i in symbols:
            countSymbols += 1
    
    data = {
        'length' : length,
        'words' : noOfWords,
        'upper' : countUpperCase,
        'lower' : countLowerCase,
        'numbers' : countNumbers,
        'symbols' : countSymbols
    }

    return render(request, 'ans.html', data)
