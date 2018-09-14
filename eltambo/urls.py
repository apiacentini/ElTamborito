"""ElTamborito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/', views.ProductView.as_view(), name="products"),
    path('productSale/', views.ProductOnSale.as_view(), name="sale"),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name="detail"),
    path('contact/', views.contact, name="contact"),
    path('product/add/', views.add_product),
    path('cart/', views.cart.as_view(), name="cart"),
    path('cart/delete/', views.delete_product),
    path('cart/singledelete/', views.delete_single_product),
    path('login2/', auth_views.login,  {'template_name': 'newLogin2.html', 'redirect_field_name': '/'}, name="login2"),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('profile/', views.profile, name="profile")
]