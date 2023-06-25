from django.contrib import admin
from .models import User
from products.admin import BasketAdmin
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение User в админ панели"""
    list_display = ('username',)
    inlines = (BasketAdmin,)

