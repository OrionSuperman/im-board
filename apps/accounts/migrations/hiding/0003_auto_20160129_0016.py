# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 00:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_info_info_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='info_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
