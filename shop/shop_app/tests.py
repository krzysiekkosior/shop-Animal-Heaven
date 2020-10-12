from django.test import TestCase
from django.urls import reverse_lazy
import pytest


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
