from django.contrib import admin

# Register your models here.
from shop_app.models import Category, Product, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
