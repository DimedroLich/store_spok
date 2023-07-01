from django.shortcuts import render, redirect

from django.contrib import auth
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView

from django.urls import reverse_lazy

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from .models import User

users = {
    'ptiza-senica': 'shmigadriga77654',
    'fedyabedya': 'helpmeimstuck1564',
    'gugugaga': 'eshkerre6542213'
}


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
    else:
        form = UserLoginForm()  # Логика, если метод = GET
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context=context)


# def registration(request):
#     """Обрабатывает страницу регистрации пользователя"""
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return redirect('users:login')
#         else:
#             print(form.errors)  # Позволяет посмотреть ошибки, если форма не проходит валидацию
#     else:
#         form = UserRegistrationForm()
#     context = {
#         'form': form
#     }
#
#     return render(request, 'users/registration.html', context=context)

class UserRegistrationView(CreateView):
    """
    Отвечает за регистрацию новых пользователей как FunctionBV-registration
    FBV отвечающий за такую же регистрацию - выше. Можно сравнить насколько CBV удобнее
    """
    model = User
    form_class = UserRegistrationForm  # Передаём класс формы для заполнения
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Store - Регистрация'}


# @login_required
# def profile(request):
#     """
#     Обрабатывает страницу профиля авторизованного пользователя.
#     Позволяет редактировать её.
#     """
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('users:profile')
#         else:
#             print(form.errors)  # Позволяет посмотреть ошибки, если форма не проходит валидацию
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     baskets = Basket.objects.filter(user=request.user)
#
#     context = {
#         'title': 'Store - Профиль',
#         'form': form,
#         'basket': baskets,  # Передача корзины в шаблон profile, который в свою очередь включает шаблон basket через тэг
#     }
#     return render(request, 'users/profile.html', context=context)


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Store - Профиль'}

    def get_context_data(self, **kwargs):
        """Добавление новых переменных и передача их в шаблон"""
        context = super(UserProfileView, self).get_context_data()
        context['basket'] = Basket.objects.filter(user=self.object)
        return context

    def get_success_url(self):
        """Куда происходит редирект при успешном изменении"""
        return reverse_lazy('users:profile', args=(self.object.id,))


def logout(request):
    """Контроллер выхода из авторизованного пользователя"""
    auth.logout(request)
    return redirect('index')
