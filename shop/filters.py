import django_filters
from django.forms import RadioSelect

from .models import Product

available_choices = (
    (True, "Да"),
    (False, "Нет"),
)


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Название товара')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Минимальная цена')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Максимальная цена')
    available = django_filters.BooleanFilter(field_name='available', label="Наличие", widget=RadioSelect())

    class Meta:
        model = Product
        fields = ['name']


# class ProductFilter_(django_filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = {
#             'name': ['icontains'],
#             'price': ['lte', 'lte'],
#             'available': []
#         }
