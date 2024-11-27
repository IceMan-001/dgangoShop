from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, CustomPasswordChangeForm, ChangePasswordForm
from django.contrib.auth.views import LoginView, AuthenticationForm, PasswordContextMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout, get_user_model
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.utils.decorators import method_decorator


User = get_user_model()
user = get_user_model()
admin = user.objects.get(username='staff')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        if self.request.user == admin:
            return reverse_lazy('admin-page')

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

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']

            # Проверка правильности старого пароля
            if not request.user.check_password(old_password):
                form.add_error('old_password', 'Старый пароль неверен.')
            else:
                # Изменение пароля
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Сохраняем сессию пользователя
                messages.success(request, 'Пароль успешно изменен.')
                return redirect('users:change_password_done')  # Замените на нужный вам URL

    else:
        form = ChangePasswordForm()

    return render(request, 'users/change_password.html', {'form': form})

class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "users/change_password_done.html"
    title = "Password change successful"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)