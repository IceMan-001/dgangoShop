from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from cart.models import CartUser
from shop.models import Product

User = get_user_model()


class Order(models.Model):
    number = models.CharField(primary_key=True, unique=True, max_length=256, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    cart = models.OneToOneField(CartUser, null=True, on_delete=models.SET_NULL, editable=False)

    status = models.CharField(max_length=50, default='в обработке')
    payment = models.CharField(max_length=50, default='картой')
    delivery = models.CharField(max_length=50, default='самовывоз из магазина')
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return " ".join(['order_', self.number])

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.ImageField()

    def get_total_price(self):
        return self.product.price * self.quantity