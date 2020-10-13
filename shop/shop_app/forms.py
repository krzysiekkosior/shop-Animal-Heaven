from django import forms
from django.forms import CharField

from .models import Category, Brand


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
