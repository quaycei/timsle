# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0012_auto_20170429_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideline',
            name='purpose',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Add Registry'), (2, 'Add Offering'), (3, 'Add User')], default=0),
        ),
        migrations.AlterField(
            model_name='guideline',
            name='registry',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registry.Registry'),
        ),
    ]