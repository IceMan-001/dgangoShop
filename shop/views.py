from lib2to3.fixes.fix_input import context
from sqlite3 import connect

from django.shortcuts import render
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DetailView,
                                  DeleteView, TemplateView)
from django.urls import reverse_lazy
from .models import Product
from .models import Category
from .forms import CategoryCreateForm, ProductCreateForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'shop/products_add.html'
    success_url = reverse_lazy('products')

class AdminTemplateView(TemplateView):
    template_name = 'shop/admin.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['total'] = 5
    #     return context


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    form = CategoryCreateForm
    template_name = 'shop/category_add.html'
    success_url = reverse_lazy('categories')


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'