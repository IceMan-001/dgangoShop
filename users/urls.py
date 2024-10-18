from django.urls import path
from .views import LoginUser, logout_user, RegisterUser, ProfileUser, ProfileUserView
from django.contrib.auth.views import LogoutView


app_name = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    # path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('profile_list/', ProfileUserView.as_view(), name='profile_list'),
]