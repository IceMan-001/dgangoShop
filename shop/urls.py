from django.conf.urls.static import static
from django.urls import path

from cart.views import cart_add
from website_shop import settings
from .views import (ProductListView, CategoryCreateView,
                    CategoryListView, ProductCreateView,
                    CategoryDetailView, ProductUpdateView,
                    CategoryUpdateView, CategoryDeleteView,
                    ProductDeleteView, ProductListByCategory,
                    ProductDetailView, ProductListViewAdmin)
from .views import product_search, product_list_view

# my_site/product/products/
urlpatterns = [
    path('categories/<slug:slug>/products/test/', product_list_view, name="test"),

    path('search/', product_search, name="product_search"),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/admin/', ProductListViewAdmin.as_view(), name='products_admin'),
    path('products/add/', ProductCreateView.as_view(), name='products_add'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:slug>/addToCart/', cart_add, name='add_to_cart'),




    path('products/categories/', CategoryListView.as_view(), name='categories'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('edit_category/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('categories/<slug:slug>/products/', ProductListByCategory.as_view(), name='products_by_category'),

    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),

]

