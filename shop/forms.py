from django import forms
from .models import Category, Product


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'created', 'updated']

        labels = {
            'description': 'Описание',
            'image': 'Изображение',
            'price': 'Цена',
            'category': 'Категория',


        }


