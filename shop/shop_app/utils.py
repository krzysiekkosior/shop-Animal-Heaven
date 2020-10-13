from django.http import Http404

from shop_app.models import Category


def get_category(pk):
    try:
        return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404
