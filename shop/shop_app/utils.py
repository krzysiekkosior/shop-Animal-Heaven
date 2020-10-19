from django.http import Http404
from shop_app.models import Category, Brand, Product, Shipment, Order


def get_category(pk):
    try:
        return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404


def get_brand(pk):
    try:
        return Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        raise Http404


def get_product(pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404


def get_shipment(pk):
    try:
        return Shipment.objects.get(pk=pk)
    except Shipment.DoesNotExist:
        raise Http404


def get_order(pk):
    try:
        return Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        raise Http404
