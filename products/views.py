from django.shortcuts import render
from .models import  Product,ProductCategory
# Create your views here.
def index(request):
    context = {
        'title' : 'Best Products from Bibasik Bobov',
        "username" : 'Bibasik Bobov',
    }
    return render(request,'products/index.html',context=context)

def products(request):
    context = {
        'title': 'Товары в магазине Бибасика Бобова',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all()
    }
    return render(request,'products/products.html',context=context)


def about_product(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'products/about_product.html',context={'product':product})