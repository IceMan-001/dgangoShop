
from django.shortcuts import render

from decimal import Decimal
from shop.models import Product

from website_shop.settings import CART_SESSION_ID


class Card:
    def __init__(self, request):
        self.session = request.session  # получаем текущую сессию
        self.user = request.user  # получаем текущего пользователя
        card = self.session.get(CART_SESSION_ID)  # получаем корзину из сессии или создаем новую
        if not card:  # создаем новую корзину
            card = self.session[CART_SESSION_ID] = {}
            self.card = card

    def save(self):
        self.session.modified = True  # метод сохранения сессии

    def add(self, product, quantity=1, override_quantity=False):  # метод помещения товара в корзину
        product_id = str(product.id)  # получаем id товара из объекта товара
        if product_id not in self.card:
            self.card[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.card[product_id]['quantity'] = quantity
        else:
            self.card[product_id]['quantity'] += quantity

        self.save()  # сохранение сессии

    def remove(self, product):  # удаление товара из корзины
        product_id = str(product.id)
        if product_id in self.card:
            del self.card[product_id]
            self.save()

    def __len__(self):  # метод подсчета количества элементов в корзине
        return sum(item['quantity'] for item in self.card.values())

    def get_total_price(self):  #
        return sum(Decimal(item['price']) * item['quantity'] for item in self.card.values())

    def clear(self):
        self.card.clear()
        # del self.session[CART_SESSION_ID]
        self.save()

    def __iter__(self):
        product_ids = self.card.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.card.copy()

        for product in products:
            cart[str(product.id)]['product'] = product


        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

