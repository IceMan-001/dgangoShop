from django.urls import path
from .views import new_quick_order, new_order, new_order_ajax, orders_list, order_detail, order_user

from .views import ListOrdersTotalUser, ListOrdersViewTotal

app_name = 'orders'

urlpatterns = [
    path('new/quick/', new_quick_order, name='new_quick_order'),   # анонимный юзер AJAX
    path('newOrder/', new_order, name="new_order"),
    path('new/', new_order_ajax, name="new_order_ajax"),
    path('list/', orders_list, name="orders"),
    path('detail/<str:number>/', order_detail, name="order_detail"),
    path('total-orders/', ListOrdersViewTotal.as_view(), name="list_orders_total"),
    path('user-orders/', order_user, name="list_orders_user"),
    path('user/orders/<str:user>/', ListOrdersTotalUser.as_view(), name="orders_user_total"),
]
