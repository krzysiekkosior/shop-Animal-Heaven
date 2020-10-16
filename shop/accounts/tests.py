import pytest
from django.test import TestCase
from django.urls import reverse_lazy

from accounts.models import Address


@pytest.mark.django_db
def test_profile_url_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('profile'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_address_as_customer(client, customer_perms, address):
    client.login(username='user', password='user1')
    response = client.get(f'/accounts/address/edit/{address.id}/')
    assert response.status_code == 200

    context = {
        'user': address.user.id,
        'city': 'Warszawa',
        'street': 'Prosta',
        'building_number': '51',
        'flat_number': 2,
        'postal_code': '00-838'
    }
    client.post(f'/accounts/address/edit/{address.id}/', context)
    assert Address.objects.first().street == 'Prosta'


@pytest.mark.django_db
def test_add_address_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_address'))
    assert response.status_code == 200

    context = {
        'user': customer_perms.id,
        'city': 'Warszawa',
        'street': 'Prosta',
        'building_number': '51',
        'flat_number': 2,
        'postal_code': '00-838'
    }
    client.post(reverse_lazy('add_address'), context)
    assert Address.objects.count() == 1


@pytest.mark.django_db
def test_delete_address_as_customer(client, customer_perms, address):
    client.login(username='user', password='user1')
    response = client.get(f'/accounts/address/delete/{address.id}/')
    assert response.status_code == 200

    client.post(f'/accounts/address/delete/{address.id}/', {'action': ''})
    assert Address.objects.count() == 1

    client.post(f'/accounts/address/delete/{address.id}/', {'action': 'delete'})
    assert Address.objects.count() == 0
