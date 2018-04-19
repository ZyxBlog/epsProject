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
    image = models.ImageField(upload_to='info/%Y/%m', verbose_name=u'工厂图', max_length=100, default='')
    size = models.CharField(choices=(('0~500人', u'0~500人'), ('500~2000人', u'500~2000人'), ('2000人以上', u'2000人以上')), max_length=30, verbose_name=u'工厂规模')
    desc = models.TextField(max_length=1000, verbose_name=u'工厂描述')

    class Meta:
        verbose_name = u'工厂信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class OrdersDetail(models.Model):
    product = models.CharField(max_length=20, verbose_name=u'产品名称')
    type = models.CharField(max_length=30, verbose_name=u'产品型号', default='')
    name = models.ForeignKey(UserProfile, verbose_name=u'用户')
    handler = models.CharField(max_length=20, verbose_name=u'经手人', default='')
    way = models.CharField(choices=(('本地提交', '本地提交'), ('远程服务提交', u'远程服务提交'), ('企业内部提交', '企业内部提交')),default=u'本地提交', max_length=20, verbose_name=u'提交方式')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'订单时间')
    num = models.IntegerField(default=0, verbose_name=u'数量')
    price = models.IntegerField(default=0, verbose_name=u'单价')
    state = models.CharField(choices=(('未完成', u'未完成'), ('已完成', u'已完成'), ('已注销', u'已注销')),
                             default='未完成', max_length=12, verbose_name=u'订单状态')
    company = models.ForeignKey(FactoryInformation, verbose_name=u'厂家')
    capacity = models.CharField(default='', verbose_name=u'体积', max_length=30)
    weight = models.CharField(default='', max_length=50, verbose_name=u'重量')

    class Meta:
        verbose_name = u'订单信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})({2})[{3}]'.format(self.name, self.product, self.state, self.time)


class ProduceTask(models.Model):
    factory = models.ForeignKey(FactoryInformation, verbose_name=u'工厂')
    product = models.CharField(default='', max_length=20, verbose_name=u'产品')
    count = models.CharField(default='0', max_length=20, verbose_name=u'成型量')
    state = models.CharField(choices=(('未执行', '未执行'), ('正在执行开发', '正在执行开发'),
                                      ('预发完成,没有成型', '预发完成,没有成型'), ('正在执行完成', '正在执行完成'),
                                      ('成型完成', '成型完成')), default=u'未执行', max_length=30, verbose_name=u'生产状态')
    raws = models.CharField(default='', max_length=20, verbose_name=u'原料类型')
    weight = models.IntegerField(default=0, verbose_name=u'容量')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'时间')

    class Meta:
        verbose_name = u'生产任务'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product


class StoreHouse(models.Model):
    weight = models.IntegerField(default=0, verbose_name=u'重量')
    version = models.CharField(default='', max_length=20, verbose_name=u'预发产品型号')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'最晚入仓时间')
    model = models.CharField(default='', max_length=20, verbose_name=u'成型产品型号')
    ratio = models.IntegerField(default=1, verbose_name=u'出料比例')
    batch = models.CharField(default='', max_length=20, verbose_name=u'批号')
    contact = models.CharField(default='', max_length=20, verbose_name=u'关联型号')
    color = models.CharField(default='', max_length=20, verbose_name=u'料颜色')

    class Meta:
        verbose_name = u'货仓存储'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.version, self.time)


class AGV(models.Model):
    name = models.CharField(default='', max_length=20, verbose_name=u'名称')
    ip = models.CharField(default='', max_length=30, verbose_name=u'ip地址')
    contact = models.CharField(choices=(('否', '否'), ('是', '是')), max_length=5, default='否', verbose_name=u'连接状态')
    route = models.IntegerField(default=1, verbose_name=u'所处路段')
    model = models.CharField(choices=(('手动', '手动'), ('自动', '自动')), default='手动', max_length=10, verbose_name=u'手动/自动模式')
    load = models.CharField(choices=(('否', '否'), ('是', '是')), default='否', max_length=10, verbose_name=u'是否负载')
    task = models.CharField(default='', max_length=20, verbose_name=u'任务名称')
    stage = models.IntegerField(default=-1, choices=((-1, '无任务空闲'), (0, '有任务但还未执行'), (1, '暂停执行'),
                                                     (2, '正在执行第一阶段fromNode'), (3, '正在执行第二阶段fromMotion'),
                                                     (4, '正在执行第三阶段toNode'), (5, '正在执行第四阶段toMotion'),
                                                     (6, '任务已经完成'), (7, '无任务自动行走到充电区')), verbose_name=u'任务执行阶段')
    error = models.IntegerField(default=0, choices=((0, '无错误'), (1, '激光雷达报警'), (2, '触边报警'), (3, '紧急开关报警')),
                                verbose_name=u'错误报警状态')
    power = models.IntegerField(default=100, verbose_name=u'电池状态')
    time = models.DateTimeField(default=datetime.now, verbose_name=u'时间')

    class Meta:
        verbose_name = u'AGV属性与状态'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.name, self.ip)
