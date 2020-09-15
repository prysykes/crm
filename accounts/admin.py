from django.contrib import admin
from . models import Customer, Product, Order, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag, TagAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'status']

admin.site.register(Order, OrderAdmin)
# Register your models here.
