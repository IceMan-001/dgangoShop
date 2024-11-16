from django.urls import path
from .views import new_quick_order, new_order, new_order_ajax, orders_list, order_detail

app_name = 'orders'

urlpatterns = [
    path('new/quick/', new_quick_order, name='new_quick_order'),   #анонимный юсер AJAX
    path('newOrder/', new_order, name="new_order"),
    path('new/', new_order_ajax, name="new_order_ajax"),
    path('list/', orders_list, name="orders"),
    path('detail/<str:number>', order_detail, name="order_detail"),
]
