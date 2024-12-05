from django.urls import path, reverse_lazy
from .views import LoginUser, logout_user, RegisterUser, ProfileUser, ProfileUserView, register_user_done, \
    change_password, PasswordChangeDoneView
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

app_name = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    # path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('profile_list/', ProfileUserView.as_view(), name='profile_list'),
    path('register_user_done/', register_user_done, name='register_user_done'),
    path('change_password/', change_password, name='change_password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(), name='change_password_done'),

    path('password-reset/',
         PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done")
         ),
         name='password_reset'),

    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete")
         ),
         name='password_reset_confirm'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),

]
