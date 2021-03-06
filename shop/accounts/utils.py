from django.http import Http404

from accounts.models import Address


def get_address(pk):
    try:
        return Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        raise Http404
