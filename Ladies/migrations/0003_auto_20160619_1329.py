# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ladies', '0002_auto_20160619_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lady',
            name='pictures',
            field=models.ImageField(upload_to='Ladies/%Y/%m/%d/'),
        ),
    ]
