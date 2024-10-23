from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product

User = get_user_model()


class CardUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CardItem(models.Model):
    card = models.ForeignKey(CardUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
