from django.contrib import admin
from .models import Product, ProductCategory, Basket

# Register your models here.


# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category',)  # Отображение полей в админке
    fields = ("name", "description", "short_description", ("price", "quantity"), "image", "category",) # Поставив поля в кортеж можно их отобразить в одну строчку
    readonly_fields = ('description',) # Поля доступные только для чтения
    search_fields = ('name', 'price',) # Поле для поиска среди объектов
    ordering = ('-quantity',) # Порядок отображения объектов



class BasketAdmin(admin.TabularInline):
    """Будет отображаться в админке users. См: users/admin.py - UserAdmin. Можно применять, если имеется ForeignKey связь"""
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0   # Количество допольнительно отображаемых пустых строк