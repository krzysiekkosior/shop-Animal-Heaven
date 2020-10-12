from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views import View

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

    def get_category(self, cat_id):
        try:
            return Category.objects.get(id=cat_id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, cat_id):
        category = self.get_category(cat_id)
        products = category.products.all().order_by('name')
        context = {
            'header': category.name,
            'products': products
        }
        return render(request, 'categories/category_details.html', context)
