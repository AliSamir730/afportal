# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_auto_20160619_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carstype',
            name='type',
            field=models.CharField(max_length=255, verbose_name='Types'),
        ),
    ]
