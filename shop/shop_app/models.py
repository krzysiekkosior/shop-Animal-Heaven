from random import randint

from django.contrib.auth.models import User
from django.db import models


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
        return self.name


class Order(models.Model):
    number = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    details = models.TextField()
    STATUS = [
        (0, "w trakcie realizacji"),
        (1, "zakończone"),
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.number} - {self.user}'


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
