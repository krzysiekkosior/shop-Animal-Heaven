from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from shop_app.forms import CategoryModelForm
from shop_app.models import Category, Product, Brand


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
        return render(request, 'categories/categories_list.html', context)


class CategoryDetailsView(View):

    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_category(pk)
        products = category.products.all().order_by('name')
        context = {
            'header': category.name,
            'products': products
        }
        return render(request, 'categories/category_details.html', context)


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

