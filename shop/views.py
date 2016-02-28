from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
# from shop.models import Product


class CategoryPage(TemplateView):
    template_name = 'category.html'


class ProductsWithCategoryPage(TemplateView):
    template_name = 'products_with_category.html'


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'