from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsViev.as_view(),name='index'),
    path('<int:product_id>/',views.about_product,name='about'),
]

