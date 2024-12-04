import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'photo']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'photo': 'Фотография',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
    new_password_1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    new_password_2 = forms.CharField(label="Повторите новый пароль", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password_1 = cleaned_data['new_password_1']
        new_password_2 = cleaned_data['new_password_2']
        old_password = cleaned_data['old_password']

        if new_password_1 and new_password_2 and new_password_1 != new_password_2:
            raise forms.ValidationError('Пароли не совпадают')

        if new_password_1 and new_password_2 and new_password_1 == new_password_2 and new_password_1 == old_password:
            raise forms.ValidationError("Пароли совпадают с текущим")

        return cleaned_data

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Старый пароль')
    new_password = forms.CharField(widget=forms.PasswordInput, label='Новый пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Подтверждение нового пароля')

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        # Проверка на совпадение нового пароля со старым
        if old_password == new_password:
            self.add_error('new_password', 'Новый пароль не должен совпадать со старым.')

        # Проверка на совпадение нового пароля с подтверждением
        if new_password != confirm_password:
            self.add_error('confirm_password', 'Пароли не совпадают.')

        return cleaned_data
