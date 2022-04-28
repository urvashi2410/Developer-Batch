from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    data = {
        'form' : form
    }
    return render(request, 'signup.html', data )