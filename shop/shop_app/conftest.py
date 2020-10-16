import pytest
from django.contrib.auth.models import User, Permission
from django.test import Client

from accounts.models import Address
from shop_app.models import Category, Brand, Product, Shipment, ShoppingCart


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def category():
    category = Category.objects.create(name='test')
    return category


@pytest.fixture
def admin_perms():
    u = User.objects.create(username='admin')
    u.set_password('admin1')
    perms = list(Permission.objects.filter(content_type_id__in=[7, 8, 9, 10, 11]))
    u.user_permissions.set(perms)
    u.save()
    return u


@pytest.fixture
def customer_perms():
    user = User.objects.create(username='user')
    user.set_password('user1')
    user.user_permissions.add(Permission.objects.get(codename='change_address'))
    user.user_permissions.add(Permission.objects.get(codename='change_shoppingcart'))
    address = Address.objects.create(user=user)
    cart = ShoppingCart.objects.create(user=user)
    user.save()
    return (user, address, cart)


@pytest.fixture
def brand():
    brand = Brand.objects.create(name='brand1', creation_year=1990)
    return brand


@pytest.fixture
def product(category, brand):
    product = Product.objects.create(
        name='product1', description='opis1', quantity=5, price=9.99,
        category=category, brand=brand
    )
    return product


@pytest.fixture
def shipment():
    shipment = Shipment.objects.create(name='shipment1', price=9.99)
    return shipment
