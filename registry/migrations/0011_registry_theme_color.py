# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 13:45
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0010_auto_20170424_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='registry',
            name='theme_color',
            field=colorful.fields.RGBColorField(default='#3f51b5'),
        ),
    ]