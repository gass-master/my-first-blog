# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_legalform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalform',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Nation', to_field='isocode'),
        ),
    ]