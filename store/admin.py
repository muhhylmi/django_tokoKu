from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Administrator Toko Ku'


class productAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "digital", "image"]
    search_fields = ["name", "price", "digital"]
    list_filter = ["digital"]
    list_per_page = 10


class customerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['user']
    list_per_page = 10


class orderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'complete']
    list_filter = ['complete']
    list_per_page = 10


class orderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'date_added']
    list_per_page = 10


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'city', 'state', 'zipcode']
    list_filter = ['state']
    list_per_page = 10


admin.site.register(Customer, customerAdmin)
admin.site.register(Product, productAdmin)
admin.site.register(Order, orderAdmin)
admin.site.register(OrderItem, orderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
