# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 06:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('seats', models.IntegerField()),
                ('seats_filled', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('games', models.ManyToManyField(to='games.Game')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1', models.CharField(default='', max_length=100)),
                ('street2', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=2)),
                ('zipcode', models.IntegerField(default=99999)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'participants',
            },
        ),
    ]
