import pytest
from django.contrib.auth.models import User
from django.test import Client
from shop_app.models import Category


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def category():
    category = Category.objects.create(name='test')
    return category