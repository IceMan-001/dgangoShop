from django.conf.urls.static import static
from django.urls import path

from website_shop import settings
from .views import (ProductListView, CategoryCreateView,
                    CategoryListView, ProductCreateView,
                    CategoryDetailView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/add/', ProductCreateView.as_view(), name='products_add'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),

    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),

]


