from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsViev.as_view(),name='index'),
    path('basket/add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>', views.basket_remove, name='basket_remove'),
    path('<int:product_id>/',views.about_product,name='about'),

]

