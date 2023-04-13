from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products,name='index'),
    path('<int:product_id>/',views.about_product,name='about'),
]

