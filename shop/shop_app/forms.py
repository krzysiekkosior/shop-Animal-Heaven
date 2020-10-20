from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Category, Brand, Product, Shipment, Order


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
        }
        error_messages = {
            'name': {
                'unique': ("Kategoria o podanej nazwie już istnieje."),
            },
        }


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'creation_date': 'Rok założenia',
        }
        error_messages = {
            'name': {
                'unique': ("Marka o podanej nazwie już istnieje."),
            },
        }


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'description': 'Opis',
            'quantity': 'Dostępna ilość',
            'price': 'Cena jednostkowa',
            'category': 'Kategoria',
            'brand': 'Marka'
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Produkt o podanej marce już istnieje.",
            }
        }


class ShipmentModelForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
        labels = {
            'name': 'Sposób dostawy',
            'price': 'Cena',
        }
        error_messages = {
            'name': {
                'unique': ("Sposób dostawy o podanej nazwie już istnieje."),
            },
        }


class OrderStatusChangeModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('status',)
        labels = {
            'status': 'Zmień status',
        }
