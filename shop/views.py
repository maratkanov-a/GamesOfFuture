from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'


class CategoryPage(TemplateView):
    template_name = 'category.html'


class ProductsWithCategoryPage(TemplateView):
    template_name = 'products_with_category.html'
