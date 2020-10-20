import pytest
from django.contrib.auth.models import Permission, User
from django.test import Client
from accounts.models import Address


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def customer_perms():
    user = User.objects.create(username='user')
    user.set_password('user1')
    user.user_permissions.add(Permission.objects.get(codename='delete_address'))
    user.user_permissions.add(Permission.objects.get(codename='change_address'))
    user.user_permissions.add(Permission.objects.get(codename='add_address'))
    user.save()
    return user


@pytest.fixture
def address(customer_perms):
    address = Address.objects.create(
        user=customer_perms,
        city='testcity1',
        street='teststreet1',
        building_number='1A',
        flat_number=1,
        postal_code='01-234'
    )
    return address
