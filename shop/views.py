from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView, DetailView, DeleteView)
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

