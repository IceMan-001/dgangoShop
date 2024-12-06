import json

from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from decimal import Decimal
from shop.models import Product, Category
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from website_shop.settings import CART_SESSION_ID
from .models import CartUser, CartItem


class Cart:
    def __init__(self, request):
        self.session = request.session  # получаем текущую сессию
        self.user = request.user  # получаем текущего пользователя
        cart = self.session.get(CART_SESSION_ID)  # получаем корзину из сессии или создаем новую
        if not cart:  # создаем новую корзину
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True  # метод сохранения сессии

    def add(self, product, quantity=1, override_quantity=False):  # метод помещения товара в корзину
        product_id = str(product.id)  # получаем id товара из объекта товара
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()  # сохранение сессии

    def remove(self, product):  # удаление товара из корзины
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):  # метод подсчета количества элементов в корзине
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):  #
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        self.cart.clear()
        del self.session[CART_SESSION_ID]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


# корзина авторизованного пользователя


class ProductCartUser:
    def __init__(self, request):
        # получаем текущего пользователя
        self.user = request.user
        # получаем корзину польз-ля из БД или создаем НОВУЮ
        self.user_cart, created = CartUser.objects.get_or_create(user=self.user)
        # получаем позиции товаров в корзине
        self.products_in_cart = CartItem.objects.filter(cart=self.user_cart)
        # создаем объект для хранения товаров
        self.cart = {}

        for item in self.products_in_cart:
            self.cart[str(item.product.id)] = {'quantity': item.quantity, 'price': item.product.price}

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    # метод сохранения корзины в БД
    def save(self):
        for prod_id in self.cart:
            product = Product.objects.get(pk=prod_id)
            # проверяем наличие товара в БД
            # если есть - обновляем кол-во
            if CartItem.objects.filter(cart=self.user_cart, product=product).exists():
                item = CartItem.objects.get(cart=self.user_cart, product=product)
                item.quantity = self.cart[prod_id]['quantity']
                item.save()
            # иначе - создаем новую позицию
            else:
                CartItem.objects.create(cart=self.user_cart, product=product, quantity=self.cart[prod_id]['quantity'])

    def remove(self, product_id, request):
        product = Product.objects.get(pk=product_id)
        cart_user = CartUser.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart_user, product=product)
        cart_item.delete()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


def cart_add(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # создаем корзину (получаем из сессии или БД)
    if request.user.id:
        cart = ProductCartUser(request)
    else:
        cart = Cart(request)

    cart.add(product=product)
    return redirect('products')


def cart_detail(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, template_name='cart/cart_detail.html', context=context)


def remove_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user.id:
        cart = ProductCartUser(request)
        cart.remove(product_id, request)
    else:
        cart = Cart(request)
        cart.remove(product)
    return redirect("cart_detail")


@csrf_exempt
def update_cart_by_front(request):
    data = json.loads(request.body)
    product_id = data.get('productIdValue')
    quantity = data.get('quantityValue')

    if product_id:
        cart = Cart(request)
        product = get_object_or_404(Product, pk=int(product_id))
        cart.add(product=product, quantity=int(quantity), override_quantity=True)
        print('ok', cart.cart)
        response_data = {'result': 'success'}
    else:
        response_data = {'result': 'failed'}

    return JsonResponse(response_data)


@csrf_exempt
def remove_product_ajax(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = data.get('productIdValue')
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    response_data = {'result': 'success'}
    return JsonResponse(response_data)


def remove_cart(request):
    """Удаление корзины у не авторизованного пользователя"""
    if not request.user.id:
        cart = Cart(request)
        cart.clear()
    else:
        cart = ProductCartUser(request)
        for item in cart.products_in_cart:
            item.delete()

    return redirect("cart_detail")
