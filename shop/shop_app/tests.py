from django.urls import reverse_lazy
import pytest

from accounts.models import Address
from shop_app.models import Category, Brand, Product, Shipment, Amount, ShoppingCart


@pytest.mark.django_db
def test_main_url(client):
    response = client.get(reverse_lazy('main'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_categories_list_url(client):
    response = client.get(reverse_lazy('cat_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_details_url(client, category):
    response = client.get(f'/category/{category.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_category_as_admin(client, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(reverse_lazy('add_category'))
    assert response.status_code == 200

    client.post(reverse_lazy('add_category'), {'name': 'test'})
    assert Category.objects.count() == 1
    assert Category.objects.first().name == 'test'


@pytest.mark.django_db
def test_no_permission_add_category_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_category'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_edit_category_as_admin(client, category, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/category/edit/{category.id}/')
    assert response.status_code == 200

    client.post(f'/category/edit/{category.id}/', {'name': 'test'})
    assert Category.objects.first().name == 'test'


@pytest.mark.django_db
def test_no_permission_edit_category_as_customer(client, category, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/category/edit/{category.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_category_as_admin(client, category, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/category/delete/{category.id}/')
    assert response.status_code == 200

    client.post(f'/category/delete/{category.id}/', {'action': ''})
    assert Category.objects.count() == 1

    client.post(f'/category/delete/{category.id}/', {'action': 'delete'})
    assert Category.objects.count() == 0


@pytest.mark.django_db
def test_no_permission_delete_category_as_customer(client, category, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/category/delete/{category.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_brands_list_url(client):
    response = client.get(reverse_lazy('brand_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_brand_details_url(client, brand):
    response = client.get(f'/brand/{brand.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_brand_as_admin(client, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(reverse_lazy('add_brand'))
    assert response.status_code == 200

    client.post(reverse_lazy('add_brand'), {'name': 'test', 'creation_year': 2020})
    assert Brand.objects.count() == 1
    assert Brand.objects.first().name == 'test'


@pytest.mark.django_db
def test_no_permission_add_brand_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_brand'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_edit_brand_as_admin(client, brand, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/brand/edit/{brand.id}/')
    assert response.status_code == 200

    client.post(f'/brand/edit/{brand.id}/', {'name': f'{brand.name}', 'creation_year': 2020})
    assert Brand.objects.first().creation_year == 2020


@pytest.mark.django_db
def test_no_permission_edit_brand_as_customer(client, brand, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/brand/edit/{brand.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_brand_as_admin(client, brand, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/brand/delete/{brand.id}/')
    assert response.status_code == 200

    client.post(f'/brand/delete/{brand.id}/', {'action': ''})
    assert Brand.objects.count() == 1

    client.post(f'/brand/delete/{brand.id}/', {'action': 'delete'})
    assert Brand.objects.count() == 0


@pytest.mark.django_db
def test_no_permission_delete_brand_as_customer(client, brand, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/brand/delete/{brand.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_products_list_url(client):
    response = client.get(reverse_lazy('product_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_details_url(client, product):
    response = client.get(f'/product/{product.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_product_as_admin(client, category, brand, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(reverse_lazy('add_product'))
    assert response.status_code == 200
    context = {
        'name': 'testproduct1',
        'description': 'testdescription1',
        'quantity': 101,
        'price': 33,
        'category': category.id,
        'brand': brand.id
    }
    client.post(reverse_lazy('add_product'), context)
    assert Product.objects.count() == 1
    assert Product.objects.first().quantity == 101


@pytest.mark.django_db
def test_no_permission_add_product_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_product'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_edit_product_as_admin(client, category, brand, product, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/product/edit/{product.id}/')
    assert response.status_code == 200
    context = {
        'name': 'testproduct1',
        'description': 'testdescription1',
        'quantity': 101,
        'price': 33,
        'category': category.id,
        'brand': brand.id
    }
    client.post(f'/product/edit/{product.id}/', context)
    assert Product.objects.first().name == 'testproduct1'


@pytest.mark.django_db
def test_no_permission_edit_product_as_customer(client, product, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/product/edit/{product.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_product_as_admin(client, product, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/product/delete/{product.id}/')
    assert response.status_code == 200

    client.post(f'/product/delete/{product.id}/', {'action': ''})
    assert Product.objects.count() == 1

    client.post(f'/product/delete/{product.id}/', {'action': 'delete'})
    assert Product.objects.count() == 0


@pytest.mark.django_db
def test_no_permission_delete_product_as_customer(client, product, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/product/delete/{product.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_shipments_list_url_as_admin(client, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(reverse_lazy('shipment_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_no_permission_shipments_list_url_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('shipment_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_add_shipment_as_admin(client, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(reverse_lazy('add_shipment'))
    assert response.status_code == 200

    client.post(reverse_lazy('add_shipment'), {'name': 'test', 'price': 12})
    assert Shipment.objects.count() == 1
    assert Shipment.objects.first().name == 'test'


@pytest.mark.django_db
def test_no_permission_add_shipment_as_customer(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_shipment'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_edit_shipment_as_admin(client, shipment, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/shipment/edit/{shipment.id}/')
    assert response.status_code == 200

    client.post(f'/shipment/edit/{shipment.id}/', {'name': f'{shipment.name}', 'price': 200})
    assert Shipment.objects.first().price == 200


@pytest.mark.django_db
def test_no_permission_edit_shipment_as_customer(client, shipment, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/shipment/edit/{shipment.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_shipment_as_admin(client, shipment, admin_perms):
    client.login(username='admin', password='admin1')
    response = client.get(f'/shipment/delete/{shipment.id}/')
    assert response.status_code == 200

    client.post(f'/shipment/delete/{shipment.id}/', {'action': ''})
    assert Shipment.objects.count() == 1

    client.post(f'/shipment/delete/{shipment.id}/', {'action': 'delete'})
    assert Shipment.objects.count() == 0


@pytest.mark.django_db
def test_no_permission_delete_shipment_as_customer(client, shipment, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/shipment/delete/{shipment.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_shopping_cart_url_as_customer(client, customer_perms, cart):
    client.login(username='user', password='user1')
    response = client.get('/cart/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_product_to_cart_as_customer(client, product, cart, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/product/{product.id}/')
    entry_products_quantity = product.quantity
    assert response.status_code == 200

    client.post(f'/product/{product.id}/', {'amount': 2})
    assert cart.products.count() == 1
    assert cart.products.first().name == 'product1'
    assert cart.products.first().quantity == entry_products_quantity - 2


@pytest.mark.django_db
def test_remove_product_from_cart_as_customer(client, customer_perms, cart, products_in_cart):
    client.login(username='user', password='user1')
    response = client.get(f'/cart/delete/{products_in_cart.product.id}/')
    assert response.status_code == 302
    assert cart.products.count() == 0


@pytest.mark.django_db
def test_add_shipment_to_cart_as_customer(client, customer_perms, cart, address, shipment, products_in_cart):
    client.login(username='user', password='user1')
    response = client.get('/cart/shipment/')
    assert response.status_code == 200
    response = client.post('/cart/shipment/', {'shipment': shipment.pk})
    assert response.status_code == 302
    cart.refresh_from_db()
    assert cart.shipment.name == shipment.name


@pytest.mark.django_db
def test_add_address_and_payment_type_to_order_as_customer(client, customer_perms, cart_with_shipment, address):
    client.login(username='user', password='user1')
    response = client.get('/cart/order/')
    assert response.status_code == 200
    response = client.post('/cart/order/', {'address': address.pk, 'payment': 0})
    assert response.status_code == 302
    cart_with_shipment.refresh_from_db()
    assert cart_with_shipment.shipment == None


@pytest.mark.django_db
def test_customers_orders_list_url(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get('/orders/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_details_url(client, customer_perms, order):
    client.login(username='user', password='user1')
    response = client.get(f'/order/{order.pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_status_change(client, admin_perms, order):
    client.login(username='admin', password='admin1')
    response = client.get(f'/order/{order.pk}/')
    assert response.status_code == 200
    client.post(f'/order/{order.pk}/', {'status': 1})
    order.refresh_from_db()
    assert order.status == 1


@pytest.mark.django_db
def test_all_orders_list_url_as_admin(client, admin_perms, order):
    client.login(username='admin', password='admin1')
    response = client.get('/all_orders/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_no_permission_all_orders_list_url_as_customer(client, customer_perms, order):
    client.login(username='user', password='user1')
    response = client.get('/all_orders/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_bank_info_url(client, customer_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/bank_info/')
    assert response.status_code == 200
