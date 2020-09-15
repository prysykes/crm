from django.shortcuts import render
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    context = {
        'customers': customers,
        'orders': orders,
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'accounts/products.html', context)

def customer(request):
    return render(request, 'accounts/customer.html')
