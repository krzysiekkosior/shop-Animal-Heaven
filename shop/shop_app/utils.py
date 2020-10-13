from django.http import Http404
from shop_app.models import Category, Brand


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
