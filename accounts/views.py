from django.shortcuts import render, get_list_or_404
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered_orders = orders.filter(status='Delivered')
    total_delivered_orders = delivered_orders.count()
    pending_orders = orders.filter(status='Pending')
    total_pending_orders = pending_orders.count()
    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'total_delivered_orders': total_delivered_orders,
        'total_pending_orders': total_pending_orders,
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'accounts/products.html', context)

def customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
    }
    
    return render(request, 'accounts/customer.html', context)
