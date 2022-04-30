from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('article_page')
    else:
        form = UserCreationForm()
    data = {
        'form' : form
    }
    return render(request, 'signup.html', data)

