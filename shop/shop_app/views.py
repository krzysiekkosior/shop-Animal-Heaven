from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from shop_app.forms import CategoryModelForm, BrandModelForm
from shop_app.models import Category, Product, Brand
from shop_app.utils import get_category, get_brand, get_product


class MainPageView(View):

    def get(self, request):
        return render(request, 'base.html')


class CategoriesListView(View):

    def get(self, request):
        categories = Category.objects.all().order_by('name')
        context = {
            'header': 'Kategorie',
            'categories': categories
        }
        return render(request, 'categories_list.html', context)


class CategoryDetailsView(View):

    def get(self, request, pk):
        category = get_category(pk)
        products = category.products.all().order_by('name')
        context = {
            'header': category.name,
            'products': products
        }
        return render(request, 'brand_or_category_details.html', context)


class CategoryAddView(PermissionRequiredMixin, View):
    permission_required = ['shop_app.add_category']

    def get(self, request):
        form = CategoryModelForm()
        context = {
            'header': 'Dodaj kategorię',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
        context = {
            'header': 'Dodaj kategorię',
            'form': form
        }
        return render(request, 'form.html', context)


class CategoryEditView(PermissionRequiredMixin, View):
    permission_required = ['shop_app.change_category']

    def get(self, request, pk):
        category = get_category(pk)
        form = CategoryModelForm(instance=category)
        context = {
            'header': 'Edytuj kategorię',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request, pk):
        category = get_category(pk)
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
        context = {
            'header': 'Edytuj kategorię',
            'form': form
        }
        return render(request, 'form.html', context)


class CategoryDeleteView(PermissionRequiredMixin, View):
    permission_required = ['shop_app.delete_category']

    def get(self, request, pk):
        category = get_category(pk)
        context = {
            'header': 'Usuń kategorię',
            'object': category
        }
        return render(request, 'delete_view.html', context)

    def post(self, request, pk):
        action = request.POST.get('action')
        if action == 'delete':
            category = get_category(pk)
            category.delete()
        return redirect('cat_list')


class BrandsListView(View):

    def get(self, request):
        brands = Brand.objects.all().order_by('name')
        context = {
            'header': 'Nasze marki',
            'brands': brands
        }
        return render(request, 'brands_list.html', context)


class BrandDetailsView(View):

    def get(self, request, pk):
        brand = get_brand(pk)
        products = brand.products.all().order_by('name')
        context = {
            'header': brand.name,
            'products': products
        }
        return render(request, 'brand_or_category_details.html', context)


class BrandAddView(PermissionRequiredMixin, View):
    permission_required = ['shop_app.add_brand']

    def get(self, request):
        form = BrandModelForm()
        context = {
            'header': 'Dodaj markę',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = BrandModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
        context = {
            'header': 'Dodaj markę',
            'form': form
        }
        return render(request, 'form.html', context)


class BrandEditView(PermissionRequiredMixin, View):
    permission_required = ['shop_app.change_brand']

    def get(self, request, pk):
        brand = get_brand(pk)
        form = BrandModelForm(instance=brand)
        context = {
            'header': 'Edytuj markę',
            'form': form
        }
        return render(request, 'form.html', context)

    def post(self, request, pk):
        brand = get_brand(pk)
        form = BrandModelForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
        context = {
            'header': 'Edytuj markę',
            'form': form
        }
        return render(request, 'form.html', context)


class BrandDeleteView(PermissionRequiredMixin, View):
    permission_required = ['shop_app.delete_brand']

    def get(self, request, pk):
        brand = get_brand(pk)
        context = {
            'header': 'Usuń markę',
            'object': brand
        }
        return render(request, 'delete_view.html', context)

    def post(self, request, pk):
        action = request.POST.get('action')
        if action == 'delete':
            brand = get_brand(pk)
            brand.delete()
        return redirect('brand_list')


class ProductsListView(View):

    def get(self, request):
        products = Product.objects.all().order_by('name')
        context = {
            'header': 'Produkty',
            'products': products
        }
        return render(request, 'products_list.html', context)


class ProductDetailsView(View):

    def get(self, request, pk):
        product = get_product(pk)
        context = {
            'header': product.name,
            'product': product
        }
        return render(request, 'product_details.html', context)
