# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', default='')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class FactoryInformation(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'工厂名称')
    product = models.CharField(max_length=20, verbose_name=u'产品名字')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    mobile = models.CharField(max_length=11, verbose_name=u'联系方式')
    contactPerson = models.CharField(max_length=15, verbose_name=u'联系人')
    address = models.CharField(max_length=20, verbose_name=u'工厂地址')
    image = models.ImageField(upload_to='info/%Y/%m', verbose_name=u'预览图', max_length=100, default='')
    size = models.CharField(choices=(('small', u'0~500人'), ('middle', u'500~2000人'), ('big', u'2000人以上')), max_length=30, verbose_name=u'工厂规模')
    desc = models.TextField(max_length=1000, verbose_name=u'工厂描述')

    class Meta:
        verbose_name = u'工厂信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class OrdersDetail(models.Model):
    product = models.CharField(max_length=20, verbose_name=u'产品名称')
    name = models.ForeignKey(UserProfile, verbose_name=u'用户')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'订单时间')
    num = models.IntegerField(default=0, verbose_name=u'数量')
    price = models.IntegerField(default=0, verbose_name=u'单价')
    state = models.CharField(choices=(('未完成', u'未完成'), ('已完成', u'已完成'), ('已注销', u'已注销')), default='未完成', max_length=12, verbose_name=u'订单状态')
    company = models.ForeignKey(FactoryInformation, verbose_name=u'厂家')

    class Meta:
        verbose_name = u'订单信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})({2})[{3}]'.format(self.name, self.product, self.state, self.time)
