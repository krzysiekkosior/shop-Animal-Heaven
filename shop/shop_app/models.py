from random import randint

from django.contrib.auth.models import User
from django.db import models

from accounts.models import Address


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creation_year = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'brand')


class Shipment(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price} zł'


class Order(models.Model):
    number = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    details = models.TextField()
    STATUS = [
        (0, "w trakcie realizacji"),
        (1, "zakończone"),
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    PAYMENTS = [
        (0, "przy odbiorze"),
        (1, "online"),
    ]
    payment = models.IntegerField(choices=PAYMENTS, null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.number} - {self.user}'

    @staticmethod
    def set_number():
        orders = Order.objects.all()
        numbers = [order.number for order in orders]
        while True:
            number = randint(1000000, 1999999)
            if number not in numbers:
                return number

    @staticmethod
    def set_details(products, total_cost, shipment):
        details = ''
        for p in products:
            details += f'<p>{p.product} - {p.amount} szt. </p>'
        details += f'<p>Sposób dostawy: {shipment.name}</p><p>Kwota zamówienia: {total_cost} zł</p>'
        return details



class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='Amount')
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, default=None)

    def is_cart_empty(self):
        return self.products.count() == 0

    def __str__(self):
        return f'Koszyk należący do {self.user}'

    def get_total_cost(self):
        total_cost = 0
        for product in self.amount_set.all():
            total_cost += product.get_cost_of_products()
        return total_cost


class Amount(models.Model):
    amount = models.IntegerField()
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} - {self.amount} szt.'

    def get_cost_of_products(self):
        return self.amount * self.product.price
