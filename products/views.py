from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product, ProductCategory, Basket
from users.models import User


# Create your views here.
# Во все классах на основе CBV в конце рекомендуется ставить View.
class IndexView(TemplateView):  # Базовый темплейт для отображения
    """CBV для отображения главной страницы магазина"""
    template_name = 'products/index.html'
    extra_context = {
        'title': 'Best Products from Bibasik Bobov',
    }


# def index(request):
#     context = {
#         'title': 'Best Products from Bibasik Bobov',
#         "username": 'Bibasik Bobov',
#     }
#     return render(request, 'products/index.html', context=context)


# def products(request, category_id=None,
#              page_number=1):  # Если категория не передаётся, то дефолтное значение = None, иначе функция будет требовать аргумент. Аргумент page - нужен для пагинатора
#     """
#     Получение списка либо всех продуктов в магазине, либо продуктов по выбранной категории
#     """
#     products = Product.objects.filter(
#         category_id=category_id) if category_id else Product.objects.all()  # Если категория передана, фильтруем товары по ней. Если нет, берём все товары
#     paginator = Paginator(object_list=products, per_page=2) # Добавление пагинатора для постраничного вывода товаров
#     products_paginator = paginator.page(page_number)
#     context = {
#         'title': 'Товары в магазине Бибасика Бобова',
#         'products': products_paginator, # Передаём именно пагинатор. Это то же самый queryset, что и был. Но с методами для работы с пагинаторами
#         'categories': ProductCategory.objects.all()
#     }
#     return render(request, 'products/products.html', context=context)

class ProductsListViev(ListView):
    """
    Отображение всех товаров из б/д
    CBV работает корректно, но для отображения фильтрованных товаров по категориям, пока вернёмся к функции
    """
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'
    extra_context = {'title': 'Товары в магазине Бибасика Бобова', }
    paginate_by = 2  # Пагинация делается настолько просто

    def get_context_data(self, *, object_list=None, **kwargs):
        """Используется для добавления ключей и дальнейшей передачи ключей в шаблон"""
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        """
        Изначально возвращает список всех продуктов
        Используется для фильтрации товаров по категориям
        Отображаемый QuerySet формируется именно в этом методе
        """
        queryset = super(ProductsListViev, self).get_queryset()
        category_id = self.kwargs.get('category_id')    # Все переданные данные хранятся в kwargs
        return queryset.filter(category_id=category_id) if category_id else queryset    # Если category_id передан, происходит фильтрация. Если нет, передаётся queryset со всеми продуктами
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
