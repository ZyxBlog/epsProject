# -*- coding: utf-8 -*-
"""epsManage URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import LoginView,  IndexView, OrdersView, DetailView, TaskView, StoreView, AGVView, RegisterView
from epsManage.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^detail/', DetailView.as_view(), name='detail'),
    url(r'^orders/$', OrdersView.as_view(), name='orders'),
    url(r'^task/$', TaskView.as_view(), name='task'),
    url(r'^store/$', StoreView.as_view(), name='store'),
    url(r'^agv/$', AGVView.as_view(), name='agv'),
    # upload image handle def
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
