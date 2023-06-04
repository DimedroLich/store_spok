from django.shortcuts import render,redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth


# Create your views here.

def login(request):
    """Обрабатывает страницу логина"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():  # Обязательная валидация при обработке POST
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)  # Аутентификация пользователся с помощью переданных через POST данных
            if user:
                auth.login(request, user)
                return redirect('index')

    form = UserLoginForm()  # Логика, если метод = GET
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    """Обрабатывает страницу регистрации пользователя"""
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context=context)

def profile(request):
    return render(request,'users/profile.html')