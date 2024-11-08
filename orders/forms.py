from django import forms
from .constans import PAYMENT_CHOISES, DELIVERY_CHOISES

class QuickOrderForms(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    last_name = forms.CharField(max_length=50, label='Фамилия')
    email = forms.EmailField(label='Эл.почта')
    phone = forms.CharField(max_length=20, label='Телефон')
    payment = forms.ChoiceField(choices=PAYMENT_CHOISES)
    delivery = forms.ChoiceField(choices=DELIVERY_CHOISES)
