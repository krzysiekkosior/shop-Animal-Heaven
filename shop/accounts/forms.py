from django import forms
from django.core.exceptions import ValidationError
import re
from accounts.models import Address


def validate_postal_code(value):
    validator = r'^[0-9]{2}-[0-9]{3}$'
    if re.search(validator, value) is None:
        raise ValidationError("Podaj poprawny kod")


class AddressModelForm(forms.ModelForm):
    postal_code = forms.CharField(validators=[validate_postal_code], label='Kod pocztowy')

    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            'city': 'Miasto',
            'street': 'Nazwa ulicy',
            'building_number': 'Numer budynku',
            'flat_number': 'Numer mieszkania',
        }
        widgets = {'user': forms.HiddenInput()}
