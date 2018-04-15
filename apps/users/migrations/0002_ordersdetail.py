# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-15 11:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u8ba2\u5355\u65f6\u95f4')),
                ('num', models.IntegerField(default=0, verbose_name='\u6570\u91cf')),
                ('price', models.IntegerField(default=0, verbose_name='\u5355\u4ef7')),
                ('state', models.IntegerField(choices=[(1, '\u672a\u5b8c\u6210'), (2, '\u5df2\u5b8c\u6210'), (3, '\u5df2\u6ce8\u9500')], default=1, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('company', models.CharField(max_length=20, verbose_name='\u5382\u5bb6')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u4fe1\u606f',
                'verbose_name_plural': '\u8ba2\u5355\u4fe1\u606f',
            },
        ),
    ]
