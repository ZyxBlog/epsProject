# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-17 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180417_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factoryinformation',
            name='size',
            field=models.CharField(choices=[('small', '0~500\u4eba'), ('middle', '500~2000\u4eba'), ('big', '2000\u4eba\u4ee5\u4e0a')], max_length=30, verbose_name='\u5de5\u5382\u89c4\u6a21'),
        ),
    ]
