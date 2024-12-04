from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser
from django.db import models


# class ProfileUserForm(forms.ModelForm):
#     username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name', 'last_name']
#         labels = {
#             'first_name': 'Имя',
#             'last_name': 'Фамилия',
#
#         }
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-input'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-input'}),
#
#         }



class ProfileUserForm(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
