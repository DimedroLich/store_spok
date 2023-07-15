import uuid
from datetime import timedelta
from django.utils.timezone import now

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User, EmailVerification


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

    def save(self, commit=True):
        """
        Служит для верификации пользователя через эл. почту перед сохранением
        """
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)  # Определяет сколько времени будет доступна ссылка для аутентификации
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()    # Вызов метода созданного нами в 'users:models'
        return user

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
