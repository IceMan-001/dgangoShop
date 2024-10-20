from django.conf.urls.static import static
from django.urls import path

from website_shop import settings
from .views import (ProductListView, CategoryCreateView,
                    CategoryListView, ProductCreateView,
                    CategoryDetailView, ProductUpdateView,
                    CategoryUpdateView, CategoryDeleteView,
                    ProductDeleteView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/add/', ProductCreateView.as_view(), name='products_add'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('edit_category/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),


    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),

]


