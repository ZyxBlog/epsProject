# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-17 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180415_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factoryinformation',
            name='image',
            field=models.ImageField(default='', upload_to='info/%Y/%m', verbose_name='\u5de5\u5382\u56fe'),
        ),
    ]