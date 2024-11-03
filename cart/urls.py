from django.urls import path

from .views import cart_detail, remove_product, update_cart_by_front, remove_cart, remove_product_ajax

urlpatterns = [
    path('detail/', cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', remove_product, name="remove_product"),
    path('update_cart_session/', update_cart_by_front, name="update_cart_session"),
    path('clear/', remove_cart, name="remove_cart_backend"),
    path('remove_fetch/', remove_product_ajax, name="remove_product_ajax"),
]
