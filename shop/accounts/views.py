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
from shop_app.models import ShoppingCart


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = f'/accounts/address/'
    template_name = 'form.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        customer = self.object
        Address.objects.create(user=customer)
        ShoppingCart.objects.create(user=customer)
        customer.user_permissions.add(Permission.objects.get(codename='change_address'))
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


class EditAddressView(PermissionRequiredMixin, View):
    permission_required = ['accounts.change_address']

    def get(self, request):
        address = Address.objects.get(user=request.user)
        form = AddressModelForm(instance=address)
        context = {
            'header': 'Adres dostawy',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request):
        address = Address.objects.get(user=request.user)
        form = AddressModelForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('main')
        context = {
            'header': 'Adres dostawy',
            'form': form
        }
        return render(request, 'form.html', context)


class CustomerProfileView(LoginRequiredMixin, View):

    def get(self, request):
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            raise Http404
        context = {
            'header': 'Informacje o koncie',
            'address': address
        }
        return render(request, 'user_profile.html', context)

