from django.urls import reverse_lazy
import pytest
from shop_app.models import Category, Brand


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
    assert Category.objects.all().count() == 1
    assert Category.objects.first().name == 'test'


@pytest.mark.django_db
def test_add_category_as_client(client, client_perms):
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
def test_edit_category_as_client(client, category, client_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_category'))
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
def test_delete_category_as_client(client, category, client_perms):
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
    assert Brand.objects.all().count() == 1
    assert Brand.objects.first().name == 'test'


@pytest.mark.django_db
def test_add_brand_as_client(client, client_perms):
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
def test_edit_brand_as_client(client, brand, client_perms):
    client.login(username='user', password='user1')
    response = client.get(reverse_lazy('add_brand'))
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
def test_delete_brand_as_client(client, brand, client_perms):
    client.login(username='user', password='user1')
    response = client.get(f'/brand/delete/{brand.id}/')
    assert response.status_code == 403
