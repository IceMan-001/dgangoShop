from django import template

from django import template

register = template.Library()


@register.filter
def string_value(product_id):
    return str(product_id)

@register.filter
def count_item(cart, product_id):
    return cart.cart[str(product_id)]['quantity']
