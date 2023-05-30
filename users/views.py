from django.shortcuts import render
from .forms import UserLoginForm


# Create your views here.

def login(request):
    form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    return render(request, 'users/registration.html')
