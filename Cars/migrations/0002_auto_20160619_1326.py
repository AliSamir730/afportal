# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Cars', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='carstype',
            options={'verbose_name': 'CarTypes', 'verbose_name_plural': 'CarTypes'},
        ),
    ]
