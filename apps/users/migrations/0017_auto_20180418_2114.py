# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-18 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180418_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersdetail',
            name='weight',
            field=models.CharField(default='', max_length=50, verbose_name='\u91cd\u91cf'),
        ),
    ]
