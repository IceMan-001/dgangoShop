from django.test import TestCase

# Create your tests here.
def cart(request):
    if request.user.id:
        return {'cart': ProductCartUser(request)}

    return {'cart': Cart(request)}
