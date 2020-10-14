"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from shop_app import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),

    path('categories/', views.CategoriesListView.as_view(), name='cat_list'),
    path('category/<int:pk>/', views.CategoryDetailsView.as_view()),
    path('category/add/', views.CategoryAddView.as_view(), name='add_category'),
    path('category/edit/<int:pk>/', views.CategoryEditView.as_view()),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view()),

    path('brands/', views.BrandsListView.as_view(), name='brand_list'),
    path('brand/<int:pk>/', views.BrandDetailsView.as_view()),
    path('brand/add/', views.BrandAddView.as_view(), name='add_brand'),
    path('brand/edit/<int:pk>/', views.BrandEditView.as_view()),
    path('brand/delete/<int:pk>/', views.BrandDeleteView.as_view()),

    path('products/', views.ProductsListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailsView.as_view()),
    path('product/add/', views.ProductAddView.as_view(), name='add_product'),
    path('product/edit/<int:pk>/', views.ProductEditView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),

]
