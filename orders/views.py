from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, get_object_or_404
import json
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from cart.views import Cart, ProductCartUser
from shop.models import Category
from .forms import OrderForm
from .models import Order, OrderItem
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView

user = get_user_model()


@csrf_exempt
def new_quick_order(request):
    data = json.loads(request.body)

    response = {"status": "ok"}

    return JsonResponse(response)


# Создание заказа АНОНИМНЫМ пользователем AJAX запросом
@csrf_exempt
def new_order_ajax(request):
    data = json.loads(request.body)
    name = data.get('name')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    delivery = data.get('delivery')
    payment = data.get('payment')

    cart = Cart(request)
    order = Order.objects.create(name=name,
                                 last_name=last_name,
                                 email=email,
                                 phone=phone,
                                 delivery=delivery,
                                 payment=payment,
                                 number=uuid.uuid4(),
                                 )
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
    # orders = OrderItem.objects.filter(order=order)
    # cart_order = cart.copy()
    cart.clear()

    url = reverse("main")
    json_response = {"status": "ok", "url": url}
    return JsonResponse(json_response)
    # return render(request, template_name='orders/order_create.html', context={'cart_order': cart_order})


def new_order(request):
    cart = ProductCartUser(request)

    if request.method == "GET":
        order_form = OrderForm()
        context = {"form": order_form}
        return render(request, template_name='orders/order_add.html', context=context)

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.number = uuid.uuid4()
            order.user = request.user
            order.cart = cart.user_cart
            order.name = request.user.username
            order.last_name = request.user.last_name
            order.email = request.user.email
            # order.phone = request.user.phone

            order.save()

            for item in cart:
                OrderItem.objects.create(order=order_form.instance, product=item['product'], quantity=item['quantity'])

            cart.user_cart.delete()

            context = {'order': order_form.instance}
            return render(request, template_name='orders/order_created.html', context=context)


@login_required
def orders_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders, 'categories': categories}

    return render(request, template_name='orders/orders.html', context=context)


@login_required
def order_detail(request, number):  # детальная информация о товаре из заказа
    admin = user.objects.get(username='staff')
    if request.user == admin:
        order = get_object_or_404(Order, number=number)
        context = {"order": order}
        return render(request, template_name='orders/order_detail.html', context=context)

    order = get_object_or_404(Order, number=number, user=request.user)
    context = {"order": order}
    return render(request, template_name='orders/order_detail.html', context=context)


def order_user(request):
    orders = Order.objects.filter(user=request.user)
    order_items = orders.order_items.all()
    context = {"orders": orders, "order_items": order_items}

    return render(request, template_name='orders/order_user.html', context=context)


class ListOrdersViewTotal(ListView):  # Получение всех заказов на странице администрирования
    model = Order
    template_name = 'orders/list_orders_total.html'
    context_object_name = 'orders'


def all_orders_list(request):
    admin = user.objects.get(username='staff')
    if request.user != admin:
        raise PermissionDenied

    orders = Order.object.all()
    context = {'orders': orders}

    return render(request, template_name='shop/list_orders_total.html', context=context)


# Домашнее задание
class ListOrdersTotalUser(ListView):
    model = Order
    template_name = 'orders/order_user.html'
    context_object_name = 'orders'
    extra_context = {
        'title': 'Все заказы пользователей'
    }

    def get_queryset(self):
        admin = user.objects.get(username='staff')
        if self.request.user == admin:
            return Order.objects.all()

        return Order.objects.filter(user=self.request.user)


class ShowDetailOrderUser(DetailView):
    model = Order
    template_name = 'orders/show_order_user.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


def show_detail_order_user(request, number):
    admin = user.objects.get(username='staff')
    if request.user == admin:
        order = get_object_or_404(Order, number=number)
        context = {"order": order}
        return render(request, template_name='orders/show_order_user.html', context=context)


def order_user_admin(request):
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders}

    return render(request, template_name='orders/order_user.html', context=context)
