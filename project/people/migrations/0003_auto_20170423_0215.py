# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170423_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
