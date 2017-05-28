# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 13:52
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0011_registry_theme_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='theme_color',
            field=colorful.fields.RGBColorField(blank=True, default=None, null=True),
        ),
    ]
