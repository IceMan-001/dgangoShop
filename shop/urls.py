from django.conf.urls.static import static
from django.urls import path

from website_shop import settings
from .views import (ProductListView, CategoryCreateView,
                    CategoryListView, ProductCreateView,
                    CategoryDetailView)

urlpatterns = [
    path('products/add', ProductCreateView.as_view(), name='products_add'),
    path('products', ProductListView.as_view(), name='products'),

    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
