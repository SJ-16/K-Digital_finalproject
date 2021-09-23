"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from vihotest2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accordeding', views.according, name='according'),
    path('ace_code_editor', views.ace_code_editor, name='ace_code_editor'),
    path('add_post', views.add_post, name='add_post'),
    path('alert', views.alert, name='alert'),
    path('animate', views.animate, name='animate'),
    path('AOS', views.AOS, name='AOS'),
    path('avatars', views.avatars, name='avatars'),
    path('base_input', views.base_input, name='base_input'),
    path('basic_card', views.basic_card, name='basic_card'),
    path('basic_template', views.basic_template, name='basic_template'),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('bookmark', views.bookmark, name='bookmark'),
    path('bootstrap_basic_table', views.bootstrap_basic_table, name='bootstrap_basic_table'),
    path('bootstrap_border_table', views.bootstrap_border_table, name='bootstrap_border_table'),
    path('bootstrap_notify', views.bootstrap_notify, name='bootstrap_notify'),
    path('box_layout', views.box_layout, name='box_layout'),
    path('login', views.login, name='login'),
    path('login_bs_tt_validation', views.login_bs_tt_validation, name='login_bs_tt_validation'),
    path('login_sa_validation', views.login_sa_validation, name='login_sa_validation'),
    path('login_bs_validation', views.login_bs_validation, name='login_bs_validation'),
    path('login_one', views.login_one, name='login_one'),
    path('login_two', views.login_two, name='login_two'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('logout', views.logout, name='logout'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up_one', views.sign_up_one, name='sign_up_one'),
    path('sign_up_two', views.sign_up_two, name='sign_up_two'),
    path('signupimpl', views.signupimpl, name='signupimpl'),
    path('search', views.search, name='search'),

]
