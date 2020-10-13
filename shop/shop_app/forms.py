from django import forms
from .models import Category


class CategoryModelForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': ('Nazwa'),
        }
        error_messages = {
            'name': {
                'unique': ("Kategoria o podanej nazwie już istnieje."),
            },
        }
