# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160129_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='bio',
            field=models.CharField(default='Bio is not Set', max_length=200),
        ),
    ]
