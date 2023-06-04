from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):
    """Форма для авторизации пользователя на URL: login"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите имя пользователя",
    }))  # Используется чтобы передать данные из шаблона. Название класса для стилей, placeholder.
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль",
    }))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    """Форма для регистрации пользователя на URL: registration"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите имя",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите фамилию",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите имя пользователя",
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите адрес эл. почты",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Подтвердите пароль",
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
    }))

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        "class": "custom-file-input",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        'readonly': True,
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
