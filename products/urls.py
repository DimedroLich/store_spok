from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListViev.as_view(), name='index'),
    path('<int:category_id>/', views.ProductsListViev.as_view(), name='category'),
    path('page/<int:page>', views.ProductsListViev.as_view(), name='paginator'),
    path('basket/add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>', views.basket_remove, name='basket_remove'),
    path('<int:product_id>/', views.about_product, name='about'),

]
