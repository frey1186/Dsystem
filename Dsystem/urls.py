"""Dsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from daily import urls as daily_urls
from Dsystem import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home, name='home'),
    url(r'^daily/', include('daily.urls', namespace='daily')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^sale/', include('sale.urls', namespace='sale')),
    url(r'^user/', include('user.urls', namespace='user')),





    url(r'^login/', views.user_login, name="login"),  # 登陆
    url(r'^logout/', views.user_logout, name="logout"),  # 登出



]
