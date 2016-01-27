# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode1', models.IntegerField()),
                ('zipcode2', models.IntegerField()),
                ('distance', models.FloatField()),
            ],
            options={
                'db_table': 'distances',
            },
        ),
    ]
