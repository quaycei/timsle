# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=20)),
                ('drop', models.IntegerField(default=20)),
            ],
        ),
    ]
