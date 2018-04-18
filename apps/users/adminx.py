# -*- coding: utf-8 -*-

__author__ = 'zyx'

import xadmin
from xadmin import views
from .models import FactoryInformation, OrdersDetail, ProduceTask


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'eps远程管理工厂系统后台'
    site_footer = 'eps远程管理工厂系统后台@created by 周轶轩'


class FactoryInformationAdmin(object):
    list_display = ['name', 'product', 'time', 'mobile', 'contactPerson', 'address', 'image', 'size', 'desc']
    search_fields = ['name', 'product', 'mobile', 'contactPerson', 'address', 'image', 'size', 'desc']
    list_filter = ['name', 'product', 'time', 'mobile', 'contactPerson', 'address', 'image', 'size', 'desc']


class OrdersDetailAdmin(object):
    list_display = ['product', 'name', 'time', 'num', 'price', 'state', 'company', 'capacity', 'weight', 'type', 'handler', 'way']
    search_fields = ['product', 'name', 'num', 'price', 'state', 'company', 'capacity', 'weight', 'type', 'handler', 'way']
    list_filter = ['product', 'name', 'time', 'num', 'price', 'state', 'company', 'capacity', 'weight', 'type', 'handler', 'way']


class ProduceTaskAdmin(object):
    list_display = ['factory', 'product', 'count', 'state', 'raws', 'weight', 'time']
    search_fields = ['factory', 'product', 'count', 'state', 'raws', 'weight']
    list_filter = ['factory', 'product', 'count', 'state', 'raws', 'weight', 'time']


xadmin.site.register(FactoryInformation, FactoryInformationAdmin)
xadmin.site.register(OrdersDetail, OrdersDetailAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(ProduceTask, ProduceTaskAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
