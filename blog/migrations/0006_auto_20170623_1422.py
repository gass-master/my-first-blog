# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_customergroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Customergroup'),
        ),
    ]
