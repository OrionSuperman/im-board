# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20160129_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='seats',
            field=models.FloatField(),
        ),
    ]
