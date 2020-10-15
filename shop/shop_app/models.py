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
    name = models.CharField(max_length=100, unique=True)
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
