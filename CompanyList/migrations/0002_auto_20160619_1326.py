# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyList', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorycompany',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
