import pytest
from django.contrib.auth.models import User, Permission
from django.test import Client

from accounts.models import Address
from shop_app.models import Category, Brand, Product, Shipment, ShoppingCart, Amount, Order


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
    customer = User.objects.create(username='user')
    customer.set_password('user1')
    customer.user_permissions.add(Permission.objects.get(codename='delete_address'))
    customer.user_permissions.add(Permission.objects.get(codename='change_address'))
    customer.user_permissions.add(Permission.objects.get(codename='add_address'))
    customer.user_permissions.add(Permission.objects.get(codename='change_shoppingcart'))
    customer.save()
    return customer


@pytest.fixture
def cart(customer_perms):
    cart = ShoppingCart.objects.create(user=customer_perms)
    return cart


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


@pytest.fixture
def cart_with_shipment(customer_perms, shipment):
    cart = ShoppingCart.objects.create(user=customer_perms, shipment=shipment)
    return cart


@pytest.fixture
def products_in_cart(product, cart, customer_perms):
    products_in_cart = Amount.objects.create(amount=2, shopping_cart=cart, product=product)
    return products_in_cart


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


@pytest.fixture
def order(customer_perms, address):
    order = Order.objects.create(
        number=123456,
        details='details',
        user=customer_perms,
        address=address
    )
    return order
