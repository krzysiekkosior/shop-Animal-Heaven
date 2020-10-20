from django.core.management import BaseCommand
from shop_app.management.commands_data.data import CATEGORIES, BRANDS, SHIPMENTS, PRODUCTS
from shop_app.models import Category, Brand, Shipment, Product


def insert_categories():
    for name in CATEGORIES:
        Category.objects.create(name=name)


def insert_brands():
    for name, creation_year in BRANDS:
        Brand.objects.create(name=name, creation_year=creation_year)


def insert_shipments():
    for name, price in SHIPMENTS:
        Shipment.objects.create(name=name, price=price)

def insert_products():
    for name, description, quantity, price, category, brand in PRODUCTS:
        Product.objects.create(
            name=name,
            description=description,
            quantity=quantity,
            price=price,
            category=Category.objects.get(name=category),
            brand=Brand.objects.get(name=brand)
        )


class Command(BaseCommand):
    help = "Insert data to database"

    def handle(self, *args, **kwargs):
        insert_categories()
        insert_brands()
        insert_shipments()
        insert_products()
        print("Data loaded successfully!")
