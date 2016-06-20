# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lady',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('pictures', models.ImageField(upload_to='%Y/%m/%d/')),
                ('reference_link', models.URLField()),
                ('LanguageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Language.language', verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='LadyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('LanguageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Language.language', verbose_name='Language')),
            ],
        ),
        migrations.AddField(
            model_name='lady',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ladies.LadyType'),
        ),
    ]
