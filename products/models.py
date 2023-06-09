from django.db import models
from django.urls import reverse
from users.models import User


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Продукт: {self.name} | Категория: {self.category}"

    def get_absolute_url(self):
        return reverse('about', kwargs={"product_id": self.id})


class Basket(models.Model):
    """Модель отвечает за представление корзины товаров в бд"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True) # Поле заполняется автоматически при создании нового объекта

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'
