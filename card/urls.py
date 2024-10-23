from django.urls import path

from .views import Cart

app_name = "cart"

urlpatterns = [
    path('cart/', Cart.as_view(), name='login'),
]