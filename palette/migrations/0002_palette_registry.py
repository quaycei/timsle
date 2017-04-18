# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
        ('palette', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='palette',
            name='registry',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registry.Registry'),
        ),
    ]