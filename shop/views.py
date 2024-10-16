from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DetailView,
                                  DeleteView, TemplateView)
from django.urls import reverse_lazy
from .models import Product, Category
from .forms import CategoryCreateForm, ProductCreateForm


class AdminTemplateView(TemplateView):  # Админская страница
    template_name = 'shop/admin.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['total'] = 5
    #     return context


class ProductCreateView(CreateView):
    model = Product  # model = Product выберет все записи из таблицы shop_product и попытается отобразить их в виде списка, используя шаблон с именем:
    # <имя приложения>/<имя модели>_list.html
    form_class = ProductCreateForm  # form_class должен ссылаться на класс формы
    template_name = 'shop/products_add.html'  # template_name – на маршрут к шаблону для отображения формы
    success_url = reverse_lazy(
        'products')  # success_url определяет маршрут перенаправления при успешной отправке после валидации формы


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    # fields = ['category', 'name', 'description', 'image', 'price']
    template_name = 'shop/edit_product.html'
    success_url = reverse_lazy('products')
    extra_context = {
        'title': 'Добавление товара',
    }


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/delete_product.html'
    success_url = reverse_lazy('products')
    extra_context = {
        'title': 'Удаление товара',
    }


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


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'shop/edit_category.html'
    success_url = reverse_lazy('categories')
    extra_context = {
        'title': 'Редактирование категории товара',
    }


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/delete_category.html'
    success_url = reverse_lazy('categories')
    extra_context = {
        'title': 'Удаление категории товара',
    }
