from django.urls import path
from .views import  logout_user
from .views import LoginUser
from django.contrib.auth.views import LogoutView


app_name = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    # path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]