from shop.views import Category


def category_in_cart(request):
    categories = Category.objects.all()
    return {'categories': categories}
