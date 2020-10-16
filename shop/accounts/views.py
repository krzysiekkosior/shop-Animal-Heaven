from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin

from accounts.forms import AddressModelForm
from accounts.models import Address
from accounts.utils import get_address
from shop_app.models import ShoppingCart


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = f'/accounts/profile/'
    template_name = 'form.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        customer = self.object
        ShoppingCart.objects.create(user=customer)
        customer.user_permissions.add(Permission.objects.get(codename='change_address'))
        customer.user_permissions.add(Permission.objects.get(codename='add_address'))
        customer.user_permissions.add(Permission.objects.get(codename='change_shoppingcart'))
        login(self.request, customer)
        return response


class CreateAdmin(SuperUserCheck, CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'form.html'

    def form_valid(self, form):
        response = super(CreateAdmin, self).form_valid(form)
        user = self.object
        perms = list(Permission.objects.filter(content_type_id__in=[7, 8, 9, 10, 11]))
        user.user_permissions.set(perms)
        return response


class AddAddressView(PermissionRequiredMixin, View):
    permission_required = ['accounts.add_address']

    def get(self, request):
        form = AddressModelForm(initial={'user': request.user})
        context = {
            'header': 'Adres dostawy',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = AddressModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context = {
            'header': 'Adres dostawy',
            'form': form
        }
        return render(request, 'form.html', context)

class EditAddressView(PermissionRequiredMixin, View):
    permission_required = ['accounts.change_address']

    def get(self, request, pk):
        address = get_address(pk)
        form = AddressModelForm(instance=address)
        context = {
            'header': 'Adres dostawy',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request, pk):
        address = get_address(pk)
        form = AddressModelForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context = {
            'header': 'Adres dostawy',
            'form': form
        }
        return render(request, 'form.html', context)


class CustomerProfileView(LoginRequiredMixin, View):

    def get(self, request):
        addresses = Address.objects.filter(user=request.user).order_by('id')
        context = {
            'header': 'Informacje o koncie',
            'addresses': addresses
        }
        return render(request, 'user_profile.html', context)

