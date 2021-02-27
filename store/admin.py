from django.contrib import admin
from .models import *

# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "digital", "image"]
    search_fields = ["name", "price", "digital"]
    list_filter = ["digital"]
    list_per_page = 4


admin.site.register(Customer)
admin.site.register(Product, productAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
