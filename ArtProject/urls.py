"""
URL configuration for ArtProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from ArtApp.views import index, search, details, user_login, register_customer, logout_view, handle_form_submission, \
    cart, place_order, confirmed, filter_arts, remove_from_cart, edit_art, add_art, delete_art

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index),
                  path('search/', search, name='search_arts'),
                  path('arts/<int:art_id>/', details, name='art_details'),
                  path('login/', user_login),
                  path('register/', register_customer),
                  path('logout/', logout_view, name='logout'),
                  path('cart/', cart, name='cart'),
                  path('deliveryinfo/', place_order, name='confirm_delivery'),
                  path('confirmed/', confirmed, name='order_confirmed'),
                  path('filter/', filter_arts, name='filter_arts'),
                  path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
                  path('art/edit/<int:art_id>/', edit_art, name='art-edit'),
                  path('add/<int:art_id>/', handle_form_submission, name='add'),
                  path('add-art/', add_art, name='add_art'),
                  path('delete-art/<int:art_id>/', delete_art, name='delete_art'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)