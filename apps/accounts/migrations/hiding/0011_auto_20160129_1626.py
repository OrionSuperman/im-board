# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 00:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20160129_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='steet2',
            new_name='street2',
        ),
    ]