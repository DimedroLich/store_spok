from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Test Title',
        "username" : 'Bibasik Bobov',
    }
    return render(request,'products/index.html',context=context)

def products(request):
    return render(request,'products/products.html')