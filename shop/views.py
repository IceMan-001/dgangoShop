from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DetailView,
                                  DeleteView, TemplateView)
from django.urls import reverse_lazy
from unicodedata import category

from .models import Product, Category
from .forms import CategoryCreateForm, ProductCreateForm

from django.db.models import Q

from django.views.generic.list import MultipleObjectMixin
from .filters import ProductFilter


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


class ListCategoriesView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'
    paginate_by = 3
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        products = Product.objects.all()
        context['categories'] = categories
        context['products'] = products

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class ProductListByCategory(ListView):
    model = Product
    template_name = 'shop/products_by_category.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['filterset'] = self.filterset

        return context

    def get_queryset(self):
        # Получаем категорию по slug из URL
        if not self.kwargs.get('slug'):
            queryset = Product.objects.all()
            self.filterset = ProductFilter(self.request.GET, queryset=queryset)
            return self.filterset.qs

        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=category)
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


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


def product_search(request):
    query = request.GET.get('query')  # получаем запрос из url
    query_text = Q(name__startswith=query) & Q(price__lt=200000) & Q(name__icontains=query)

    results = Product.objects.filter(query_text)
    categories = Category.objects.all()

    context = {'categories': categories, 'products': results}

    return render(request, template_name="shop/home.html", context=context)


# class AboutView(ListView):
#     template_name = 'shop/about.html'
#     extra_context = {
#         'title': 'Страница о нас',
#     }


def about(request):
    context = {
        'name': 'Ivan',
        'lastname': 'Ivanov',
        'email': 'ivanivanov@yandex.ru',
        'title': 'Страница о нас',
    }
    return render(request, template_name='shop/about.html', context=context)


def contact(request):
    context = {
        'name': 'Ivan',
        'lastname': 'Ivanov',
        'email': 'ivanivanov@yandex.ru',
        'title': 'Страница контактов',
    }
    return render(request, template_name='shop/contact.html', context=context)


def product_list_view(request, slug):
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products_by_slug = Product.objects.filter(category=category)
        filterset = ProductFilter(request.GET, queryset=products_by_slug)
        context = {'products': filterset.qs, 'filterset': filterset, 'categories': categories}
        return render(request, template_name='shop/product_by_category.html', context=context)

    queryset = Product.objects.all()
    filterset = ProductFilter(request.GET, queryset=queryset)
    context = {'products': filterset.qs, 'filterset': filterset, 'categories': categories}
    return render(request, template_name='shop/product_by_category.html', context=context)
