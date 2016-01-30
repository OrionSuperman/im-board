# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160129_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='info',
            name='address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
