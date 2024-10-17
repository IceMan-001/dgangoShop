from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginUserForm
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import  logout



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('products')


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')


