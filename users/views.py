from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout, get_user_model
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied

User = get_user_model()


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('products')


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:register_user_done')


def register_user_done(request):
    return render(request, 'users/register_done.html')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile_list')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/profile_list.html'
    extra_context = {'title': "Информация о пользователе"}
