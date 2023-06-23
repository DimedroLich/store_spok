from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory, Basket
from users.models import User


# Create your views here.

def index(request):
    context = {
        'title': 'Best Products from Bibasik Bobov',
        "username": 'Bibasik Bobov',
    }
    return render(request, 'products/index.html', context=context)


# class ProductsViev(ListView):
#     """
#     Отображение всех товаров из б/д
#     CBV работает корректно, но для отображения фильтрованных товаров по категориям, пока вернёмся к функции
#     """
#     template_name = 'products/products.html'
#     model = Product
#     context_object_name = 'products'
#     extra_context = {'title': 'Товары в магазине Бибасика Бобова', }
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = ProductCategory.objects.all()
#         return context


def products(request, category_id=None,
             page_number=1):  # Если категория не передаётся, то дефолтное значение = None, иначе функция будет требовать аргумент. Аргумент page - нужен для пагинатора
    """
    Получение списка либо всех продуктов в магазине, либо продуктов по выбранной категории
    """
    products = Product.objects.filter(
        category_id=category_id) if category_id else Product.objects.all()  # Если категория передана, фильтруем товары по ней. Если нет, берём все товары
    paginator = Paginator(object_list=products, per_page=2) # Добавление пагинатора для постраничного вывода товаров
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Товары в магазине Бибасика Бобова',
        'products': products_paginator, # Передаём именно пагинатор. Это то же самый queryset, что и был. Но с методами для работы с пагинаторами
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context=context)


@login_required  # Проверка залогинен ли пользователь если нет, происходит редирект на страницу логина. Страница редиректа указана в settings
def basket_add(request, product_id):
    """Контроллер добавления продукта в корзину товаров. Называется 'обработчик событий'"""
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():  # Если в корзине нет никаких товаров
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:  # Если есть, увеличиваем количество товара на 1
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return redirect(request.META['HTTP_REFERER'])  # Возвращение на ту страницу, где пользователь выполнял действие


@login_required
def basket_remove(request, basket_id):
    """Контроллер обработчик события. Удаление товара из корзины"""
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])  # Возвращение на ту страницу, где пользователь выполнял действие


def about_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/about_product.html', context={'product': product})
