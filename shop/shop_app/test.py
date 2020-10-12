from django.test import TestCase
from django.urls import reverse_lazy
import pytest


@pytest.mark.django_db
def test_main_url(client):
    response = client.get(reverse_lazy('main'))
    assert response.status_code == 200
