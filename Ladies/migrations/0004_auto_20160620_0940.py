# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ladies', '0003_auto_20160619_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lady',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='lady',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='lady',
            name='pictures',
            field=models.ImageField(upload_to='Ladies/%Y/%m/%d/', verbose_name='Pictures'),
        ),
        migrations.AlterField(
            model_name='lady',
            name='reference_link',
            field=models.URLField(verbose_name='Reference URL'),
        ),
        migrations.AlterField(
            model_name='lady',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='ladytype',
            name='type',
            field=models.CharField(max_length=255, verbose_name='Tool Types'),
        ),
    ]