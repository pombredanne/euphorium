# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('engine', models.CharField(max_length=255)),
                ('origin_url', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
