from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    """Модель проверки верификации пользователя"""
    code = models.UUIDField(unique=True)  # Поле формирования универсального идентификатора
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)  # Дата и время в поле заполняется автоматически
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        send_mail(
            "Subject here",
            "Test verification email",
            "from@example.com",
            [self.user.email],
            fail_silently=False,
        )
