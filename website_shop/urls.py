"""
URL configuration for website_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website_shop import settings
from django.conf.urls.static import static
from shop.views import AdminTemplateView, ProductCreateView, ProductListView, about, contact, admin_page
from orders.views import all_orders_list

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),  # корень сайта
    path('staff/', admin_page, name='admin-page'),
    path('staff/orders/', all_orders_list, name='admin_all_orders'),
    path('admin/', admin.site.urls),
    # include() -> группировала маршрутов, относящихся к одной категории
    path('product/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    # path('ssession', views.setsession),
    # path('gsession', views.getsession),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "shop.views.forbidden"
handler404 = "shop.views.page_not_found"
handler500 = "shop.views.server_error"
