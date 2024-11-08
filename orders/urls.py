from django.urls import path
from .views import new_quick_order

urlpatterns = [
    path('new/quick/', new_quick_order, name='new_quick_order'),

]