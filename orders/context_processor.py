from .forms import QuickOrderForms

def quick_order_form(request):
    return ('quick_order_form': QuickOrderForms())

