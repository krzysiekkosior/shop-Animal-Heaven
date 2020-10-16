from django.contrib import admin

# Register your models here.
from shop_app.models import Category, Product, Brand, Shipment, Order, ShoppingCart, Amount

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Shipment)
admin.site.register(Order)
admin.site.register(ShoppingCart)
admin.site.register(Amount)
